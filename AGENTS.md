# Repository conventions

This repository distributes shared skills to Codex and Claude Code.

- Keep `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`
  aligned: same marketplace name, plugin order, names, and source directories.
- Treat each root `plugins/<name>/plugin.json` as the canonical identity. Mirror
  common metadata in that plugin's `.claude-plugin/plugin.json`.
- Keep each plugin self-contained. Bundle referenced resources inside its root.
- When shipped plugin content changes, update its version in both manifests.
- Keep validator tooling on the Python standard library. Run the two validation
  commands in README.md after changing manifests, catalogs, skills, or tooling.
- Read `docs/adding-plugins.md` before adding a plugin or a new component type.
