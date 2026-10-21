import json
import tempfile
import unittest
from pathlib import Path

from scripts.sync_mermaid_docs import sync_docs


class MermaidSyncTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="mermaid-sync-test-")
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.source = root / "upstream"
        self.plugin = root / "plugin"
        self.syntax = self.source / "docs/syntax"
        self.config = self.source / "docs/config"
        self.references = self.plugin / "skills/mermaid/references"
        for directory in (self.syntax, self.config, self.references, self.plugin / ".claude-plugin"):
            directory.mkdir(parents=True)
        self.manifests = [self.plugin / "plugin.json", self.plugin / ".claude-plugin/plugin.json"]
        for manifest in self.manifests:
            manifest.write_text(json.dumps({"name": "mermaid", "version": "1.0.0"}))
        (self.plugin / "skills/mermaid/SKILL.md").write_text("[Flowchart](references/flowchart.md)\n")
        (self.syntax / "flowchart.md").write_text(
            "[Theme](../config/theming.md#colors)\n"
            "[Icons](../config/icons.md)\n"
            "[Schema](/config/schema-docs/config)\n"
            "[Flowchart](./flowchart.md)\n"
            "[Source](../../packages/mermaid/src/docs/syntax/flowchart.md)\n"
            "![Example](img/example.png)\n"
            "```mermaid\nflowchart TD\n A --> B\n```\n"
        )
        for name in ("configuration", "directives", "layouts", "math", "theming", "tidy-tree"):
            (self.config / f"{name}.md").write_text(f"# {name}\n")
        (self.config / "directives.md").write_text("[Config](./configuration.md)\n")

    def test_sync_rewrites_links_and_bumps_both_versions(self):
        (self.references / "obsolete.md").write_text("Old documentation.\n")
        self.assertTrue(sync_docs(self.source, self.plugin))
        self.assertFalse((self.references / "obsolete.md").exists())
        content = (self.references / "flowchart.md").read_text()
        self.assertIn("[Theme](config-theming.md#colors)", content)
        self.assertIn("https://mermaid.js.org/config/icons.html", content)
        self.assertIn("https://mermaid.js.org/config/schema-docs/config", content)
        self.assertIn("[Flowchart](./flowchart.md)", content)
        self.assertIn("https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/flowchart.md", content)
        self.assertIn("[Example](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/img/example.png)", content)
        self.assertIn("```mermaid\nflowchart TD\n A --> B\n```", content)
        self.assertEqual((self.references / "config-directives.md").read_text(), "[Config](config-configuration.md)\n")
        for manifest in self.manifests:
            self.assertEqual(json.loads(manifest.read_text())["version"], "1.0.1")
        self.assertEqual((self.plugin / "skills/mermaid/SKILL.md").read_text(), "[Flowchart](references/flowchart.md)\n")

    def test_unchanged_sync_does_not_rewrite_manifests(self):
        sync_docs(self.source, self.plugin)
        before = {manifest: manifest.read_bytes() for manifest in self.manifests}
        self.assertFalse(sync_docs(self.source, self.plugin))
        for manifest in self.manifests:
            self.assertEqual(manifest.read_bytes(), before[manifest])

    def test_missing_documentation_leaves_package_unchanged(self):
        for missing in (self.syntax / "flowchart.md", self.config / "theming.md"):
            with self.subTest(missing=missing.name):
                content = missing.read_text()
                missing.unlink()
                (self.references / "existing.md").write_text("Keep me.\n")
                with self.assertRaises(ValueError):
                    sync_docs(self.source, self.plugin)
                self.assertEqual((self.references / "existing.md").read_text(), "Keep me.\n")
                self.assertEqual(json.loads(self.manifests[0].read_text())["version"], "1.0.0")
                missing.write_text(content)

    def test_missing_skill_reference_leaves_package_unchanged(self):
        (self.plugin / "skills/mermaid/SKILL.md").write_text("[Missing](references/missing.md)\n")
        with self.assertRaisesRegex(ValueError, "missing.md"):
            sync_docs(self.source, self.plugin)
        self.assertEqual(list(self.references.iterdir()), [])

    def test_manifest_version_drift_leaves_package_unchanged(self):
        self.manifests[1].write_text(json.dumps({"name": "mermaid", "version": "1.0.2"}))
        with self.assertRaisesRegex(ValueError, "versions"):
            sync_docs(self.source, self.plugin)
        self.assertEqual(list(self.references.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
