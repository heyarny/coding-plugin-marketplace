# Ponytail

All eight skills from the installed **Engineering Suite Ponytail 2.0.0** plugin,
bundled as one plugin for Codex and Claude Code. This marketplace package starts
at version **1.0.0** in **Developer Tools**.

| Skill | Purpose |
| --- | --- |
| `entry-ponytail` | Route a request to the appropriate bundled workflow |
| `ponytail` | Apply the simplest solution that preserves required behavior; supports lite, full, and ultra |
| `ponytail-review` | Report unnecessary complexity in a diff |
| `ponytail-audit` | Report over-engineering across a repository |
| `ponytail-debt` | Collect deliberate `ponytail:` shortcuts into a ledger |
| `ponytail-gain` | Display historical upstream benchmark results with their limitations |
| `ponytail-help` | Show modes, commands, and update instructions |
| `code-simplification` | Refactor for clarity while preserving behavior |

## Install

From the marketplace repository root:

```sh
codex plugin marketplace add .
codex plugin add ponytail@coding-plugins-marketplace
```

For Claude Code:

```sh
claude plugin marketplace add .
claude plugin install ponytail@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, select Ponytail and describe the task, for example:

> Use Ponytail Audit to find unnecessary complexity in this repository.

In Claude Code, invoke a skill with its plugin namespace:

```text
/ponytail:entry-ponytail Audit this repository for over-engineering.
/ponytail:ponytail lite
/ponytail:ponytail-review
/ponytail:ponytail-debt
/ponytail:ponytail-help
```

The `ponytail` mode stays active within the conversation until you say
“stop ponytail” or “normal mode”. Review and audit report findings; simplification
workflows can edit project files and run validation. The debt workflow reports
markers and writes a ledger only when requested. Follow the project's permission
and Git conventions, including any requirements for explicit commits.

## Dependencies and scope

Uses the host's file, shell, Git, and project validation tools. No MCP server,
credentials, executable hooks, or extra plugin installation is required.
This is the skills-only Engineering Suite bundle. The original standalone
Ponytail project's startup hooks and default-mode configuration are not included.

`ponytail-gain` reports historical upstream benchmark results, not measured savings
in your project. Its source and caveats are bundled in
[benchmark provenance](skills/ponytail-gain/references/benchmarks.md).

## Source and attribution

Engineering Suite's source manifest credits **Saul Martí**. The six Ponytail modes
come from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail);
`code-simplification` comes from
[Addy Osmani's agent skills](https://github.com/addyosmani/agent-skills).
**Arnold Stark** maintains this marketplace packaging.

[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records the source bundle version,
upstream commits, and original skill checksums. Six skill files are retained
unchanged; help is adapted for this marketplace and the gain
skill receives local provenance and a benchmark cost correction. See
[third-party notices](THIRD_PARTY_NOTICES.md) for the complete change list.

This is a vendored snapshot. Updating the marketplace installs this package's
published version; it does not independently fetch upstream skills.

Licensed under [MIT](LICENSE), with the preserved
[Ponytail license](third_party_licenses/ponytail-LICENSE) and
[Addy Osmani license](third_party_licenses/addy-LICENSE).
