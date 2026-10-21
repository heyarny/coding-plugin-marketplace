# Brainstorm

A thinking partner for exploring ideas, comparing alternatives, and refining a
direction through conversation. Applies across topics, from a small personal
decision to an organizational, creative, or technical question.

Version **1.0.0**. Category: **Developer Tools**. Author: **Arnold Stark**.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add brainstorm@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install brainstorm@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, select Brainstorm and describe the idea or decision:

> Use Brainstorm to compare ways to share reusable components across our apps.
> Show a simple approach and distinct alternatives using the same example.

In Claude Code:

```text
/brainstorm:brainstorm Compare ways to share reusable components across our apps.
```

Expect concrete examples, clear tradeoffs, and a comparison that develops as you
respond. The skill can use a compact table, ASCII drawing, or Mermaid diagram
when it helps explain relationships. Once the constraints are clear, it recommends
a direction and identifies a useful next decision or experiment.

## Behavior and dependencies

The skill carries accepted constraints forward, asks focused questions when
needed, and revisits choices when new evidence warrants it. Brainstorming stays
exploratory; implementation or saving a decision note requires a request.

Conversation alone is sufficient. File tools help ground an existing-system
discussion; web search can verify external facts; local subagents can explore
independent perspectives when delegation is useful and allowed. These are
optional host capabilities. Exploratory delegation stays read-only unless changes
are already authorized. Diagrams can be returned as text without a renderer.

This package has no MCP servers, executable hooks, credentials, or required
external services. No other plugin installation is required.

## Packaging

The supplied skill's instruction body is preserved unchanged. Its folded YAML
description is normalized to an equivalent single-line quoted string for this
repository's lightweight validator. Both clients use the shared
`skills/brainstorm/` directory; each has its own matching manifest.

Licensed under [MIT](LICENSE).
