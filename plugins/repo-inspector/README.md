# Repo Inspector

A starter plugin that maps a repository before development work. Its shared
`repo-map` skill inspects instructions, source files, and build configuration.
It uses the host's file and shell tools; it has no MCP servers, hooks, or external
service dependencies.

After installing from this marketplace:

- **Codex:** ask “Use Repo Inspector to map this repository.”
- **Claude Code:** run `/repo-inspector:repo-map`.

Expected result: a concise repository map with file references and discovered
validation commands. The workflow keeps repository files unchanged.

`plugin.json` is the portable manifest; `.claude-plugin/plugin.json` carries the
same identity for Claude Code. Both load the same `skills/` directory.
