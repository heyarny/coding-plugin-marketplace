# GrillMe

All eight skills from **Engineering Suite GrillMe 2.0.0**, packaged for Codex
and Claude Code. This marketplace package is version **1.0.0**, under
**Productivity**.

| Skill | Purpose |
| --- | --- |
| `entry-grill-me` | Route to the appropriate bundled workflow |
| `grill-me` | Sharpen a plan or design through an interview |
| `grill-with-docs` | Combine the interview with a domain glossary and architectural decisions |
| `grilling` | Explore a design tree in rounds of questions with recommended answers |
| `domain-modeling` | Clarify terms and record domain definitions and consequential decisions |
| `idea-refine` | Explore variations, evaluate directions, and draft an idea one-pager |
| `interview-me` | Discover and confirm the user's underlying intent one question at a time |
| `loop-me` | Design recurring workflows and maintain their specifications |

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add grill-me@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install grill-me@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, select GrillMe and describe your idea or plan:

> Use GrillMe to challenge my plan for sharing reusable components across our apps.

The entry workflow chooses `grill-with-docs` for an explicit grill request in a
working repository and `grill-me` elsewhere. It uses `idea-refine` for ideation
and `interview-me` for discovering intent. You can also request a specific mode.

In Claude Code:

```text
/grill-me:entry-grill-me Challenge this feature idea until the decisions are clear.
/grill-me:grill-me Stress-test my plan.
/grill-me:grill-with-docs Review this design and capture our terminology and decisions.
/grill-me:interview-me Help me uncover what I actually need.
/grill-me:loop-me Design my weekly planning workflow.
```

The outputs depend on the mode: clarified decisions, a confirmed statement of
intent, an idea one-pager, a glossary, ADRs, or workflow specifications. The
package focuses on design; final implementation is a separate task.

## Dependencies and file changes

These are interactive workflows that need a responsive user. Repository-grounded
interviews use host file tools and local subagents for fact-finding. Equivalent
question, file-search, and file-read tools are used in each client. No other
plugin installation, MCP server, credentials, or external service is required.

Document-producing modes can change project files:

- `domain-modeling` maintains `CONTEXT.md` and can create `docs/adr/*.md` as
  terms and consequential decisions are resolved.
- `loop-me` creates, edits, or deletes `workflows/*.md` as the design evolves and
  maintains `NOTES.md`. It does not create automations or run those workflows.
- `idea-refine` saves `docs/ideas/<idea-name>.md` after confirmation;
  `interview-me` saves `docs/intent/<topic>.md` only when requested and confirmed.

Idea Refine includes an optional Bash helper that creates `docs/ideas/` in the
target project. It is bundled inside the skill and is not a lifecycle hook.
Resolve its installed path as described in the skill and run it with the target
project as the working directory.

## Source and attribution

Engineering Suite's source manifest credits **Saul Martí**. The grilling and
domain-modeling workflows come from
[Matt Pocock's skills](https://github.com/mattpocock/skills); Idea Refine and
Interview Me come from
[Addy Osmani's agent skills](https://github.com/addyosmani/agent-skills).
**Arnold Stark** maintains this marketplace packaging.

[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records the source plugin version,
relevant upstream commits, and original file hashes. Bundled resource paths and
tool references are adapted for both clients; see
[third-party notices](THIRD_PARTY_NOTICES.md) for the change list. This is a
vendored snapshot, so marketplace updates do not independently fetch upstream.

Licensed under [MIT](LICENSE), with the preserved
[Matt Pocock license](third_party_licenses/aihero-LICENSE) and
[Addy Osmani license](third_party_licenses/addy-LICENSE).
