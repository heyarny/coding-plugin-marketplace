#!/usr/bin/env python3
"""Sync bundled Mermaid documentation from a checked-out source repository."""

import argparse
import json
import re
import shutil
from pathlib import Path

from scripts.validate_marketplace import VERSION, require


CONFIG_NAMES = ("configuration", "directives", "layouts", "math", "theming", "tidy-tree")
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")


def fix_links(content, filename, filenames):
    section = "config" if filename.startswith("config-") else "syntax"

    def replace(match):
        image, label, target = match.groups()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)
        if target.startswith("../../packages/mermaid/src/docs/"):
            target = "https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/" + target.removeprefix("../../packages/mermaid/src/docs/")
        elif target.startswith("/"):
            target = "https://mermaid.js.org" + target
        else:
            clean = target.split("#", 1)[0].split("?", 1)[0]
            suffix = target[len(clean):]
            if clean.removeprefix("./") in filenames:
                return match.group(0)
            if clean.startswith(("./img/", "img/")):
                target = "https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/" + section + "/" + clean.removeprefix("./") + suffix
            else:
                name = Path(clean).name
                bundled = ("config-" if "/config/" in clean or section == "config" else "") + name
                if bundled in filenames:
                    target = bundled + suffix
                else:
                    website_path = clean[3:] if clean.startswith("../") else section + "/" + clean.removeprefix("./")
                    if website_path.endswith(".md"):
                        website_path = website_path[:-3] + ".html"
                    target = "https://mermaid.js.org/" + website_path + suffix
        return "[" + (label or "Example image") + "](" + target + ")"

    parts = re.split(r"(^```[^\n]*\n.*?^```[^\n]*$)", content, flags=re.MULTILINE | re.DOTALL)
    return "".join(part if index % 2 else LINK.sub(replace, part) for index, part in enumerate(parts))


def sync_docs(source, plugin):
    sources = {path.name: path for path in (source / "docs/syntax").glob("*.md")}
    require(bool(sources), "No Mermaid syntax documentation found")
    for name in CONFIG_NAMES:
        path = source / f"docs/config/{name}.md"
        require(path.is_file(), f"Missing Mermaid configuration reference: {path}")
        sources[f"config-{name}.md"] = path
    contents = {name: fix_links(path.read_text(encoding="utf-8"), name, sources)
                for name, path in sources.items()}
    skill = plugin / "skills/mermaid/SKILL.md"
    for target in re.findall(r"\]\(references/([^)]+)\)", skill.read_text(encoding="utf-8")):
        require(target.split("#", 1)[0] in contents, f"Missing skill reference: {target}")
    manifests = [plugin / "plugin.json", plugin / ".claude-plugin/plugin.json"]
    metadata = [json.loads(path.read_text(encoding="utf-8")) for path in manifests]
    version = metadata[0].get("version")
    require(isinstance(version, str) and VERSION.fullmatch(version)
            and version == metadata[1].get("version"), "Plugin versions must match stable MAJOR.MINOR.PATCH")
    references = skill.parent / "references"
    current = {path.name: path.read_text(encoding="utf-8") for path in references.glob("*.md")}
    if current == contents:
        return False
    major, minor, patch = version.split(".")
    if references.exists():
        shutil.rmtree(references)
    references.mkdir(parents=True)
    for name, content in contents.items():
        (references / name).write_text(content, encoding="utf-8")
    for path, manifest in zip(manifests, metadata):
        manifest["version"] = f"{major}.{minor}.{int(patch) + 1}"
        path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Mermaid repository checkout")
    parser.add_argument("--plugin", type=Path, default=Path(__file__).resolve().parents[1] / "plugins/mermaid")
    args = parser.parse_args()
    try:
        changed = sync_docs(args.source, args.plugin)
    except (ValueError, OSError, UnicodeError) as error:
        parser.exit(1, f"Mermaid sync failed: {error}\n")
    print("Synced Mermaid references and bumped both plugin versions." if changed else "Mermaid references are unchanged.")


if __name__ == "__main__":
    main()
