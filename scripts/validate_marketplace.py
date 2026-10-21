#!/usr/bin/env python3
"""Check this repository's local, skills-only marketplace conventions."""

import argparse
import json
import re
import sys
from pathlib import Path


SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)")
COMMON_FIELDS = ("name", "version", "description", "keywords")
OPTIONAL_FIELDS = ("author", "license")
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)
    except (OSError, ValueError, UnicodeError) as error:
        raise ValueError(f"{path}: {error}") from error
    require(isinstance(value, dict), f"{path}: expected a JSON object")
    return value


def text_field(data, key, context):
    value = data.get(key)
    require(isinstance(value, str) and bool(value.strip()), f"{context}: missing or empty {key}")
    return value


def object_field(data, key, context):
    value = data.get(key)
    require(isinstance(value, dict), f"{context}: {key} must be an object")
    return value


def local_directory(root, source):
    require(isinstance(source, str), "source path must be a string")
    require(source.startswith("./") and ".." not in source.split("/") and "\\" not in source,
            f"source path must start with ./ and stay inside its root: {source}")
    target = (root / source).resolve()
    require(target.is_relative_to(root.resolve()), f"source path escapes its root: {source}")
    require(target.is_dir(), f"source directory does not exist: {source}")
    return target


def catalog_entries(catalog, root, client):
    entries = catalog.get("plugins")
    require(isinstance(entries, list) and bool(entries), f"{client}: plugins must be a nonempty array")
    indexed = {}
    for entry in entries:
        require(isinstance(entry, dict), f"{client}: each plugin entry must be an object")
        name = text_field(entry, "name", client)
        require(SLUG.fullmatch(name), f"{client}: invalid plugin name: {name}")
        require(name not in indexed, f"{client}: duplicate plugin: {name}")
        source = entry.get("source")
        if client == "Codex":
            require(isinstance(source, dict) and source.get("source") == "local",
                    f"{name}: Codex source must be a local source object")
            source = source.get("path")
            policy = object_field(entry, "policy", name)
            require(policy.get("installation") == "AVAILABLE", f"{name}: installation must be AVAILABLE")
            require(policy.get("authentication") in ("ON_INSTALL", "ON_USE"),
                    f"{name}: invalid authentication policy")
            text_field(entry, "category", name)
        local_directory(root, source)
        require(source == f"./plugins/{name}", f"{name}: source must be ./plugins/{name}")
        indexed[name] = source
    return indexed


def validate_skill(path):
    content = path.read_text(encoding="utf-8")
    parts = content.split("---\n", 2)
    require(content.startswith("---\n") and len(parts) == 3, f"{path}: missing skill frontmatter")
    header, body = parts[1:]
    names = re.findall(r"^name: ([a-z0-9]+(?:-[a-z0-9]+)*)$", header, re.MULTILINE)
    require(names == [path.parent.name], f"{path}: skill name must match its directory")
    descriptions = re.findall(r"^description: (\S.*)$", header, re.MULTILINE)
    description_error = f"{path}: description must be nonempty single-line text (plain or JSON double-quoted)"
    require(len(descriptions) == 1, description_error)
    description = descriptions[0]
    if description.startswith('"'):
        try:
            description = json.loads(description)
        except ValueError as error:
            raise ValueError(description_error) from error
    else:
        require(description[0] not in "'|>#", description_error)
    require(isinstance(description, str) and bool(description.strip())
            and "\n" not in description and "\r" not in description, description_error)
    require(bool(body.strip()), f"{path}: skill instructions are empty")


def validate_plugin(root, name, category):
    for resource in root.rglob("*"):
        require(not resource.is_symlink(), f"{resource}: bundle regular files instead of symlinks")
    portable = read_json(root / "plugin.json")
    claude = read_json(root / ".claude-plugin/plugin.json")
    require(portable.get("$schema") == SCHEMA, f"{name}: missing portable manifest schema")
    for field in COMMON_FIELDS:
        require(field in portable and field in claude and portable[field] == claude[field],
                f"{name}: manifests disagree on {field}")
    for field in OPTIONAL_FIELDS:
        require((field in portable) == (field in claude)
                and portable.get(field) == claude.get(field),
                f"{name}: manifests disagree on {field}")
    require(portable["name"] == name, f"{name}: manifest name differs from catalog")
    version = text_field(portable, "version", name)
    require(VERSION.fullmatch(version), f"{name}: version must use stable MAJOR.MINOR.PATCH")
    text_field(portable, "description", name)
    if "license" in portable:
        text_field(portable, "license", name)
    if "author" in portable:
        text_field(object_field(portable, "author", name), "name", name)
    keywords = portable["keywords"]
    require(isinstance(keywords, list) and bool(keywords)
            and all(isinstance(item, str) and item.strip() for item in keywords),
            f"{name}: keywords must be a nonempty array of strings")
    extensions = object_field(portable, "extensions", name)
    interface = object_field(object_field(extensions, "com.openai", name), "interface", name)
    for field in ("displayName", "shortDescription", "longDescription"):
        text_field(interface, field, name)
    if "developerName" in interface:
        text_field(interface, "developerName", name)
    require(interface.get("category") == category, f"{name}: listing category differs from catalog")
    require((root / "README.md").is_file(), f"{name}: missing plugin README.md")
    skills = root / "skills"
    require(skills.is_dir(), f"{name}: missing skills directory")
    directories = sorted(path for path in skills.iterdir() if path.is_dir())
    require(bool(directories), f"{name}: plugin must contain at least one skill")
    for directory in directories:
        path = directory / "SKILL.md"
        require(path.is_file(), f"{name}: missing {path.relative_to(root)}")
        validate_skill(path)


def validate_marketplace(root):
    root = Path(root).resolve()
    codex = read_json(root / ".agents/plugins/marketplace.json")
    claude = read_json(root / ".claude-plugin/marketplace.json")
    name = text_field(codex, "name", "marketplace")
    require(SLUG.fullmatch(name), "marketplace name must be lowercase kebab-case")
    require(claude.get("name") == name, "marketplace names differ between clients")
    text_field(object_field(codex, "interface", "Codex"), "displayName", "Codex")
    text_field(object_field(claude, "owner", "Claude Code"), "name", "Claude Code")
    codex_entries = catalog_entries(codex, root, "Codex")
    claude_entries = catalog_entries(claude, root, "Claude Code")
    require(codex_entries == claude_entries and list(codex_entries) == list(claude_entries),
            "catalog plugin names, order, or sources differ between clients")
    directories = {path.name for path in (root / "plugins").iterdir() if path.is_dir()}
    require(directories == set(codex_entries), "plugins directory and catalog entries differ")
    for entry in codex["plugins"]:
        validate_plugin(root / entry["source"]["path"], entry["name"], entry["category"])
    return len(codex_entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        count = validate_marketplace(args.root)
    except (ValueError, OSError, UnicodeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    print(f"Validated {count} plugin(s) for Codex and Claude Code.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
