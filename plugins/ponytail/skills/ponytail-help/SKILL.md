---
name: ponytail-help
description: "Quick-reference card for all ponytail modes, skills, and commands. One-shot display, not a persistent mode. Trigger: /ponytail-help, \"ponytail help\", \"what ponytail commands\", \"how do I use ponytail\"."
disable-model-invocation: true
---

# Ponytail Help

Display this reference card when invoked. One-shot, do NOT change mode,
write flag files, or persist anything.

## Levels

| Level | Trigger | What change |
|-------|---------|-------------|
| **Lite** | `/ponytail lite` | Build what's asked, name the lazier alternative in one line. |
| **Full** | `/ponytail` | The ladder enforced: YAGNI → stdlib → native → one line → minimum. Default. |
| **Ultra** | `/ponytail ultra` | YAGNI extremist. Deletion before addition. Challenges requirements before building. |

Level sticks until changed or session end.

## Skills

| Skill | Trigger | What it does |
|-------|---------|--------------|
| **ponytail** | `/ponytail` | Lazy mode itself. Simplest solution that works. |
| **ponytail-review** | `/ponytail-review` | Over-engineering review: `L42: yagni: factory, one product. Inline.` |
| **ponytail-audit** | `/ponytail-audit` | Whole-repo over-engineering audit: ranked list of what to delete. |
| **ponytail-debt** | `/ponytail-debt` | Harvest `ponytail:` shortcut comments into a tracked ledger. |
| **ponytail-gain** | `/ponytail-gain` | Measured-impact scoreboard: less code, less cost, more speed. |
| **ponytail-help** | `/ponytail-help` | This card. |

In Codex, select this marketplace's Ponytail plugin and name the workflow,
for example "Use Ponytail Review on this diff".
In Claude Code, qualify the commands above with the plugin name:
`/ponytail:ponytail`, `/ponytail:ponytail-review`, and
`/ponytail:ponytail-help`. Other bundled skills use the same namespace.

## Deactivate

Say "stop ponytail" or "normal mode". Resume anytime with `/ponytail`.
`/ponytail off` also works.

## Activation

This marketplace bundles skills only. Invoke Ponytail to activate its `full`
mode, or specify `lite` or `ultra`. The mode persists within the conversation
until changed or deactivated. Standalone Ponytail startup hooks and its
environment/config-file default-mode settings are not included here.

## Update

Update `coding-plugins-marketplace` through your client's marketplace manager,
then update or reinstall its `ponytail` plugin and start a new session. For a
local marketplace checkout, pull the repository changes first. This package is
a vendored snapshot; its updates do not independently fetch upstream skills.

## More

Full docs + examples: https://github.com/DietrichGebert/ponytail
