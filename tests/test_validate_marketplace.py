import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_marketplace import validate_marketplace


CODEX_CATALOG = ".agents/plugins/marketplace.json"
CLAUDE_CATALOG = ".claude-plugin/marketplace.json"
PLUGIN = "plugins/repo-inspector"
PORTABLE = f"{PLUGIN}/plugin.json"
CLAUDE_MANIFEST = f"{PLUGIN}/.claude-plugin/plugin.json"


class MarketplaceValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="marketplace-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write_json(CODEX_CATALOG, {
            "name": "test-marketplace",
            "interface": {"displayName": "Test Marketplace"},
            "plugins": [{
                "name": "repo-inspector",
                "source": {"source": "local", "path": f"./{PLUGIN}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Productivity",
            }],
        })
        self.write_json(CLAUDE_CATALOG, {
            "name": "test-marketplace",
            "owner": {"name": "Test Publisher"},
            "plugins": [{"name": "repo-inspector", "source": f"./{PLUGIN}"}],
        })
        identity = {
            "name": "repo-inspector", "version": "0.1.0",
            "description": "A test workflow.", "author": {"name": "Test Publisher"},
            "license": "MIT", "keywords": ["test"],
        }
        self.write_json(CLAUDE_MANIFEST, identity)
        self.write_json(PORTABLE, {
            **identity,
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "extensions": {"com.openai": {"interface": {
                "displayName": "Test Plugin", "shortDescription": "A test workflow",
                "longDescription": "Describe the test workflow.",
                "developerName": "Test Publisher", "category": "Productivity",
            }}},
        })
        (self.root / PLUGIN / "README.md").write_text("# Test Plugin\n")
        skill = self.root / PLUGIN / "skills/repo-map/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("---\nname: repo-map\ndescription: Map a repository.\n---\n\nRead the README.\n")

    def write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def edit_json(self, relative, change):
        path = self.root / relative
        value = json.loads(path.read_text())
        change(value)
        path.write_text(json.dumps(value))

    def test_valid_package_is_accepted(self):
        self.assertEqual(validate_marketplace(self.root), 1)

    def test_package_without_author_or_license_is_accepted(self):
        for manifest in (PORTABLE, CLAUDE_MANIFEST):
            self.edit_json(manifest, lambda value: [value.pop(field) for field in ("author", "license")])
        self.edit_json(PORTABLE, lambda value: value["extensions"]["com.openai"]["interface"].pop("developerName"))
        self.assertEqual(validate_marketplace(self.root), 1)

    def test_optional_metadata_drift_is_rejected(self):
        for field in ("author", "license"):
            with self.subTest(field=field):
                original = (self.root / CLAUDE_MANIFEST).read_text()
                self.edit_json(CLAUDE_MANIFEST, lambda value: value.pop(field))
                with self.assertRaisesRegex(ValueError, f"manifests disagree on {field}"):
                    validate_marketplace(self.root)
                (self.root / CLAUDE_MANIFEST).write_text(original)

    def test_invalid_optional_metadata_is_rejected(self):
        for field, invalid in (("author", {"name": ""}), ("license", "")):
            with self.subTest(field=field):
                originals = {manifest: (self.root / manifest).read_text() for manifest in (PORTABLE, CLAUDE_MANIFEST)}
                for manifest in originals:
                    self.edit_json(manifest, lambda value: value.update({field: invalid}))
                with self.assertRaises(ValueError):
                    validate_marketplace(self.root)
                for manifest, content in originals.items():
                    (self.root / manifest).write_text(content)

    def test_empty_developer_name_is_rejected(self):
        self.edit_json(PORTABLE, lambda value: value["extensions"]["com.openai"]["interface"].update(developerName=""))
        with self.assertRaisesRegex(ValueError, "missing or empty developerName"):
            validate_marketplace(self.root)

    def test_duplicate_plugin_is_rejected(self):
        self.edit_json(CODEX_CATALOG, lambda value: value["plugins"].append(value["plugins"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate plugin"):
            validate_marketplace(self.root)

    def test_missing_plugin_directory_is_rejected(self):
        shutil.rmtree(self.root / PLUGIN)
        with self.assertRaisesRegex(ValueError, "directory does not exist"):
            validate_marketplace(self.root)

    def test_parent_traversal_is_rejected(self):
        self.edit_json(CODEX_CATALOG, lambda value: value["plugins"][0]["source"].update(path="./../outside"))
        with self.assertRaisesRegex(ValueError, "stay inside its root"):
            validate_marketplace(self.root)

    def test_absolute_source_is_rejected(self):
        self.edit_json(CLAUDE_CATALOG, lambda value: value["plugins"][0].update(source=str(self.root / PLUGIN)))
        with self.assertRaisesRegex(ValueError, "stay inside its root"):
            validate_marketplace(self.root)

    def test_catalog_name_drift_is_rejected(self):
        self.edit_json(CLAUDE_CATALOG, lambda value: value.update(name="other-marketplace"))
        with self.assertRaisesRegex(ValueError, "marketplace names differ"):
            validate_marketplace(self.root)

    def test_manifest_version_drift_is_rejected(self):
        self.edit_json(CLAUDE_MANIFEST, lambda value: value.update(version="0.2.0"))
        with self.assertRaisesRegex(ValueError, "manifests disagree on version"):
            validate_marketplace(self.root)

    def test_invalid_version_is_rejected(self):
        for manifest in (PORTABLE, CLAUDE_MANIFEST):
            self.edit_json(manifest, lambda value: value.update(version="01.0.0"))
        with self.assertRaisesRegex(ValueError, "MAJOR.MINOR.PATCH"):
            validate_marketplace(self.root)

    def test_missing_skill_is_rejected(self):
        (self.root / PLUGIN / "skills/repo-map/SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "missing skills/repo-map/SKILL.md"):
            validate_marketplace(self.root)

    def test_skill_name_drift_is_rejected(self):
        path = self.root / PLUGIN / "skills/repo-map/SKILL.md"
        path.write_text(path.read_text().replace("name: repo-map", "name: different-skill"))
        with self.assertRaisesRegex(ValueError, "skill name must match"):
            validate_marketplace(self.root)

    def test_empty_quoted_skill_description_is_rejected(self):
        path = self.root / PLUGIN / "skills/repo-map/SKILL.md"
        path.write_text(path.read_text().replace("description: Map a repository.", 'description: ""'))
        with self.assertRaisesRegex(ValueError, "description must be nonempty"):
            validate_marketplace(self.root)

    def test_duplicate_json_key_is_rejected(self):
        (self.root / PORTABLE).write_text('{"name":"repo-inspector","name":"other"}')
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            validate_marketplace(self.root)

    def test_invalid_catalog_type_is_rejected(self):
        self.edit_json(CODEX_CATALOG, lambda value: value.update(plugins={}))
        with self.assertRaisesRegex(ValueError, "plugins must be a nonempty array"):
            validate_marketplace(self.root)

    def test_bundled_symlink_is_rejected(self):
        (self.root / PLUGIN / "outside.md").symlink_to(self.root / CLAUDE_CATALOG)
        with self.assertRaisesRegex(ValueError, "instead of symlinks"):
            validate_marketplace(self.root)


if __name__ == "__main__":
    unittest.main()
