# Mermaid

Generate Mermaid diagram code from a description or requirements. The shared
`mermaid` skill covers 23 diagram types, including flowcharts, sequence diagrams,
class diagrams, ER diagrams, Gantt charts, and architecture diagrams. It consults
bundled syntax and configuration references before producing a `mermaid` code
block with appropriate styling.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add mermaid@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install mermaid@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, ask:

> Use Mermaid to create a flowchart for a user login process.

In Claude Code:

```text
/mermaid:mermaid draw a sequence diagram for API authentication
/mermaid:mermaid ER diagram for an e-commerce database
```

Expected output: Mermaid source in a fenced code block, ready to paste into a
compatible Markdown preview or Mermaid renderer.

## Behavior and dependencies

The host needs file tools to read the packaged references. The skill can write
or edit a diagram file when requested. Generating code uses the bundled
references without credentials or a network connection. Rendering or exporting
a diagram requires a separate Mermaid-compatible viewer; available syntax
depends on that viewer's Mermaid version. Links to supplementary documentation
and example images open external upstream resources.

This package contains skill instructions and documentation. It has no MCP
servers, executable hooks, or external service integrations. `plugin.json`
provides the portable Codex identity, and `.claude-plugin/plugin.json` provides
the matching Claude Code identity. Both clients use `skills/mermaid/`.

## Documentation sync

The marketplace's GitHub Action refreshes syntax and configuration references
from `mermaid-js/mermaid` every Sunday at 00:00 UTC. It can also be run manually.
When documentation changes, it fixes reference links, increments the patch
version in both manifests, validates the marketplace, and commits the update.

I forked this plugin from [thdk/mermaid-skill](https://github.com/thdk/mermaid-skill).

Author: Arnold Stark. Licensed under [MIT](LICENSE).
