# CodebaseDesign

The full **Engineering Suite CodebaseDesign 2.0.0** bundle for Codex and Claude
Code, with its interview dependencies included locally. This marketplace package
is version **1.0.0**, under **Developer Tools**.

| Skill | Purpose |
| --- | --- |
| `entry-codebase-design` | Route to module design, architecture review, or explicitly requested TypeScript setup |
| `codebase-design` | Design deep modules, their interfaces, seams, adapters, and tests |
| `improve-codebase-architecture` | Find architecture improvements, produce an HTML report, and refine a selected candidate |
| `setup-ts-deep-modules` | Install and verify TypeScript package boundary checks when explicitly requested |
| `grilling` | Internal dependency for exploring a candidate's design decisions |
| `domain-modeling` | Internal dependency for maintaining domain terminology and consequential decisions |

The first four skills come from the CodebaseDesign bundle. The last two are
dependencies of its architecture-review workflow, copied from Engineering Suite
GrillMe at the same upstream commit. A separate GrillMe installation is not
required.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add codebase-design@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install codebase-design@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, select CodebaseDesign and describe the design question:

> Use CodebaseDesign to identify shallow modules in this repository and help me
> choose one interface to improve.

In Claude Code:

```text
/codebase-design:entry-codebase-design Help me choose where the seam and interface should live.
/codebase-design:codebase-design Compare alternative interfaces for this module.
/codebase-design:improve-codebase-architecture Find architecture improvements in this repository.
```

Request TypeScript setup explicitly when you want it:

```text
/codebase-design:setup-ts-deep-modules Set up deep module boundaries in this TypeScript project.
```

Expected outputs include interface proposals, comparisons of alternative designs,
an architecture-review report, domain glossary entries, and ADRs. The TypeScript
setup mode produces executable package-boundary checks and an example package.

## Dependencies and file changes

Design workflows use host file tools, Git history, an interactive user, and local
subagents. The alternative-interface workflow calls for at least three independent
design agents. No MCP server or account credentials are required.

The architecture scan writes an HTML report to the OS temporary directory and
opens it for review. Its supplied report scaffold loads Tailwind and Mermaid from
CDNs, so rendering those styles and diagrams needs network access. After you
select a candidate, the bundled interview can update `CONTEXT.md` and create
`docs/adr/*.md` as terms and decisions are resolved.

The explicitly requested TypeScript setup needs Node.js and the project's package
manager. It installs `dependency-cruiser` as a development dependency, creates or
merges `.dependency-cruiser.cjs`, adds `lint:boundaries`, connects it to existing
checks, and creates an example package with tests. It also documents the package
convention and adds a pointer from `CLAUDE.md` or `AGENTS.md`. Repository permission
and Git conventions apply to this work.

Installing this plugin does not run the setup workflow. Its dependency-cruiser
configuration is a bundled template, with no executable lifecycle hooks.

## Source and attribution

Engineering Suite's source manifest credits **Saul Martí**. The design, setup,
grilling, and domain-modeling skills come from
[Matt Pocock's skills](https://github.com/mattpocock/skills).
**Arnold Stark** maintains this marketplace packaging.

[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records the source bundles, upstream
commit, and original file hashes. Local skill links replace host-specific
`Skill` tool calls; the workflow content, invocation policies, supporting
references, and configuration template are otherwise preserved. See
[third-party notices](THIRD_PARTY_NOTICES.md) for the change list.

Licensed under [MIT](LICENSE), with the preserved
[Matt Pocock license](third_party_licenses/aihero-LICENSE).
