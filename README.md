# Coding Plugins Marketplace

A Git-based marketplace of reusable coding plugins for **Codex** and **Claude
Code**. Plugin content is shared; each client gets its own catalog and manifest.

| Plugin | Category | Workflow | Dependencies |
| --- | --- | --- | --- |
| [Review and Track Findings](plugins/review-and-track-findings/README.md) | Developer Tools | Review changes and track findings through repair and verification | Host Git, file, and validation tools; subagents for parallel reviews |
| [Git Commit](plugins/git-commit/README.md) | Developer Tools | Draft Conventional Commit messages or commit staged changes | Host Git and shell tools |
| [Flutter Tools](plugins/flutter-tools/README.md) | Developer Tools | Inspect running Flutter apps and diagnose motion with two bundled skills | Dart/Flutter MCP; native UI tools; macOS Simulator and ffmpeg for motion capture |
| [Coordinate Codex Agents](plugins/coordinate-codex-agents/README.md) | Developer Tools | Coordinate Codex app chats across saved projects | Host-provided Codex app task-management APIs |
| [Ponytail](plugins/ponytail/README.md) | Developer Tools | Simplify code, review and audit complexity, and track deliberate shortcuts with eight bundled skills | Host file, shell, Git, and project validation tools |
| [Repo Inspector](plugins/repo-inspector/README.md) | Developer Tools | Map repository structure, entry points, and validation commands | Host file and shell tools |
| [Mermaid](plugins/mermaid/README.md) | Productivity | Generate Mermaid diagrams from requirements using bundled syntax references | Host file tools; Mermaid renderer for visual previews |
| [Brainstorm](plugins/brainstorm/README.md) | Productivity | Explore ideas, compare alternatives, and refine a direction through conversation | Conversation; optional file, web search, and local subagent tools |
| [GrillMe](plugins/grill-me/README.md) | Productivity | Challenge plans, clarify intent, and develop domain models or workflow specs with eight bundled skills | Interactive user; host file, question, and local subagent tools; Bash for the optional helper |
| [CodebaseDesign](plugins/codebase-design/README.md) | Developer Tools | Design module interfaces, review architecture, and optionally enforce TypeScript package boundaries | Host repository tools and local subagents; Node.js and a package manager for explicit TypeScript setup; network for report CDNs |

Categories describe the broad purpose of each plugin and match in both catalogs.
Manifest keywords identify specific workflows, such as code review, refactoring,
Git commits, Flutter debugging, agent coordination, planning, and documentation.

## Install and use

Install directly from GitHub. Add the marketplace once, then install the plugins
you want from the table above.

**Codex CLI**

```sh
codex plugin marketplace add heyarny/coding-plugin-marketplace
codex plugin add repo-inspector@coding-plugins-marketplace
```

Start a new session and ask “Use Repo Inspector to map this repository.”
Use `/plugins` to browse and manage plugins.

**Claude Code**

```sh
claude plugin marketplace add heyarny/coding-plugin-marketplace
claude plugin install repo-inspector@coding-plugins-marketplace
```

Start a new session and run `/repo-inspector:repo-map`.
Replace `repo-inspector` in the install command with another plugin name from
the table; each plugin's README has its usage examples and dependencies.

## Develop locally

After cloning this repository, check the catalog from the repository root with
Python 3.11 or newer:

```sh
python3 scripts/validate_marketplace.py
python3 -m unittest discover -s tests -v
```

Register the local marketplace and install the starter plugin:

**Codex CLI**

```sh
codex plugin marketplace add .
codex plugin add repo-inspector@coding-plugins-marketplace
```

Start a new session and ask “Use Repo Inspector to map this repository.”
The `/plugins` browser also lets you inspect and manage installed plugins.

**Claude Code**

```sh
claude plugin validate .
claude plugin marketplace add .
claude plugin install repo-inspector@coding-plugins-marketplace
```

Start a new session and run `/repo-inspector:repo-map`. During development,
you can also load it directly with `claude --plugin-dir ./plugins/repo-inspector`.

## Repository layout

```text
.agents/plugins/marketplace.json       Codex catalog
.claude-plugin/marketplace.json        Claude Code catalog
plugins/
  repo-inspector/
    plugin.json                       Portable manifest for Codex
    .claude-plugin/plugin.json         Claude Code manifest
    skills/repo-map/SKILL.md           Shared instructions
    README.md                         Usage and dependencies
scripts/validate_marketplace.py        Catalog and package consistency checks
tests/                                Validator regression tests
docs/                                 Authoring and GitHub publishing guides
.github/                              CI, dependency updates, contribution templates
```

Catalog source paths resolve from the repository root. Plugin components live
inside their plugin directory so installations also work from a cached copy.

## Add plugins and publish

Follow [Adding plugins](docs/adding-plugins.md).
The starter uses repository-local sources, independent plugin versions, and
optional installation. CI checks catalog alignment and package completeness.
The validator covers this repository's skills-only layout; use client validation
and installation tests as well before releasing changes.

[Publishing to GitHub](docs/publishing.md) covers repository creation, installation
from GitHub, and releases. GitHub distribution makes this catalog available to
people with repository access. Listing in either vendor's public directory is a
separate submission process.

## Format references

- [OpenAI plugin packaging and marketplace metadata](https://developers.openai.com/plugins/build/plugins)
- [Claude Code marketplace creation](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [GitHub Actions security guidance](https://docs.github.com/en/actions/reference/security/secure-use)

Licensed under [MIT](LICENSE).
