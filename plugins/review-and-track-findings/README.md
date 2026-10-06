# Review and Track Findings

Review staged, unstaged, and untracked code changes and track actionable findings
in a living repository document. This plugin bundles the `review-and-track-findings`
skill, its issue template, and its Codex display metadata for both Codex and
Claude Code.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add review-and-track-findings@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install review-and-track-findings@coding-plugins-marketplace
```

Start a new session after installation.

## Use

In Codex, ask:

> Use Review and Track Findings to review my current changes and record actionable
> findings in code_review_issues.md.

In Claude Code, invoke the namespaced skill:

```text
/review-and-track-findings:review-and-track-findings Review my current changes and track actionable findings.
```

Then continue with requests such as:

- “Explain nr. 2 and whether its value justifies the fix.”
- “Fix CR-002 and verify the result.”
- “Remove the review document if all findings are resolved.”

You can supply a different review scope or document path in the request.

## Behavior and dependencies

The default output is `<repository-root>/code_review_issues.md`. A new document
is created only when actionable findings exist. An existing document is resumed
with stable IDs such as `CR-001`, preserving earlier evidence and decisions.
Each finding records its impact, evidence, recommended repair, value versus
complexity, acceptance criteria, and resolution history.

Reviews and explanations can create or update the issue document. Source-code
changes require a fix request. The document is retained until the user explicitly
requests deletion and every finding is resolved under the skill's closure rules.
The workflow can run project validation commands; fixes and checks depend on the
target project's tools and runtime.

The host supplies Git inspection, file access, and shell or equivalent tools.
Reviews with at least two independent questions request two or three inspect-only
subagents; parallel review requires host support for subagents. The skill requests
`xhigh` reasoning effort and calls for disclosure when that effort is unavailable.
The host determines agent capabilities and permission policies.
This package has no MCP servers, hooks, credentials, or external service dependencies.

All referenced resources live inside the skill directory, including
[`assets/review-issues-template.md`](skills/review-and-track-findings/assets/review-issues-template.md).
The original skill instructions and bundled resources are preserved from the
supplied local skill. `plugin.json` provides the portable Codex identity, and
`.claude-plugin/plugin.json` provides the matching Claude Code identity.

Licensed under [MIT](LICENSE).
