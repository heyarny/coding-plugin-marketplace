# Debug

The full **Engineering Suite Debug 2.0.0** bundle for Codex and Claude Code.
This marketplace package is version **1.0.0**, under **Developer Tools**.

| Skill | Purpose |
| --- | --- |
| `entry-debug` | Route to diagnosis, regression tests, browser or performance checks, or an active merge conflict |
| `diagnosing-bugs` | Build a tight reproduction loop, minimize the failure, test hypotheses, and verify the fix |
| `debugging-and-error-recovery` | Triage test failures, build errors, and unexpected runtime behavior |
| `tdd` | Agree test seams and implement one failing-test-to-fix slice at a time |
| `test-driven-development` | Discover the project's testing stack and apply regression-testing patterns |
| `codebase-design` | Consult module, interface, seam, and adapter vocabulary when choosing test boundaries |
| `browser-testing-with-devtools` | Inspect browser state, console output, network traffic, screenshots, and traces |
| `resolving-merge-conflicts` | Resolve an existing merge or rebase using the intent of both changes |
| `performance-optimization` | Establish a baseline, locate bottlenecks, and keep changes only when measurements justify them |

Includes testing and mocking examples, module-design references, a performance
checklist, and a Bash template for reproduction steps that need a human.
All bundled workflow dependencies are local to this plugin.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add debug@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install debug@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, select Debug and describe the failure:

> Use Debug to reproduce this regression, identify the root cause, and fix it
> with a regression test.

In Claude Code:

```text
/debug:entry-debug Find why this browser flow is failing.
/debug:diagnosing-bugs Diagnose this intermittent export failure.
/debug:performance-optimization Measure and investigate this latency regression.
```

Expected outputs include a reproducible failure command, ranked hypotheses,
root-cause evidence, a verified fix, and regression coverage at an appropriate
test seam. Performance work includes before/after measurements and a record of
kept or reverted attempts.

## Dependencies and file changes

General diagnosis uses host file and shell tools, Git, the target project's
runtime and test commands, and access to an environment that reproduces the bug.
Some workflows ask the user to confirm test seams or provide observations.
Complex regression tests and alternative-interface design can use local
subagents; alternative-interface design calls for at least three design agents.

Browser workflows additionally need **Chrome DevTools MCP** configured in the
host, Chrome, Node.js, and `npx`. The bundled
[browser skill](skills/browser-testing-with-devtools/SKILL.md#setting-up-chrome-devtools-mcp)
contains separate Codex `.codex/config.toml` and Claude Code `.mcp.json` examples.
Package download needs network access. This package contains skills and resources;
it does not install or launch the MCP server automatically. Backend and CLI
diagnosis can run without it.

The diagnosis workflow can create tests, reproduction scripts, temporary
instrumentation, and captured artifacts, then edit source files and remove
temporary debug code. Copy and customize the
[human-in-the-loop template](skills/diagnosing-bugs/scripts/hitl-loop.template.sh)
in the target project before running it in an interactive Bash terminal. It asks
the user for actions and observations and prints captured answers; credentials
must stay out of captured output. No account credentials are required by the
plugin itself; testing an authenticated application may require a test account.

Performance work can create a `PERF.md` ledger and propose monitoring or CI
budgets. The merge-conflict workflow is only for an existing merge/rebase and
includes staging resolved work and completing that operation. Follow the user's
Git authorization and repository conventions when running these workflows.
Installation does not execute these actions or register lifecycle hooks.

## Source and attribution

Engineering Suite's source manifest credits **Saul Martí**. The bundle includes
skills from [Matt Pocock](https://github.com/mattpocock/skills) and
[Addy Osmani](https://github.com/addyosmani/agent-skills).
**Arnold Stark** maintains this marketplace packaging.

[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records the source bundle, upstream
commits, and original file hashes. Local adaptations add portable skill links,
client-specific MCP setup, a resolved helper path, and an optional review-stage
reference. Original skill frontmatter and UI metadata are preserved.
See [third-party notices](THIRD_PARTY_NOTICES.md) for details.

Licensed under [MIT](LICENSE), with preserved licenses for
[Matt Pocock](third_party_licenses/aihero-LICENSE) and
[Addy Osmani](third_party_licenses/addy-LICENSE).
