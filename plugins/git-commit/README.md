# Git Commit

Turn staged changes into a concise Conventional Commit message. Include `draft`
to preview the message; invoking the workflow without `draft` requests a commit
on the current branch.

## Install

From the marketplace repository root:

```sh
# Codex CLI
codex plugin marketplace add .
codex plugin add git-commit@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add .
claude plugin install git-commit@coding-plugins-marketplace
```

Start a new session after installation.

## Use

Stage the changes you want included before invoking the skill. In Codex, ask:

> Use Git Commit draft to propose a Conventional Commit message for my staged changes.

When you want it to commit, ask:

> Use Git Commit to commit my staged changes on the current branch.

In Claude Code:

```text
/git-commit:git-commit draft
```

For a commit, invoke `/git-commit:git-commit` without `draft`.

## Behavior and dependencies

The skill inspects the current Git index only. It uses the narrowest suitable
commit type and adds a scope or a short bullet body when the staged changes
warrant them. If nothing is staged, it reports that and stops.

For unrelated staged concerns, it recommends a split and asks for a decision
before changing the index or committing. Approved splits can unstage and restage
the relevant files or hunks. A normal commit changes the current branch's history;
`draft` returns the proposed message without committing. The skill leaves
unstaged and untracked work out of the message and does not push.

The host needs Git and shell access to a repository with a working index.
Permission policies and repository hooks apply when a commit runs. This package
has no MCP servers, bundled executable hooks, credentials, or external service
dependencies.

The supplied skill instructions are preserved unchanged. The Codex launch prompt
includes `draft` so it previews a message without committing.
`plugin.json` supplies the portable Codex identity, and
`.claude-plugin/plugin.json` supplies the matching Claude Code identity. Both
clients use the shared `skills/git-commit/` directory.

Author: Arnold Stark. Licensed under [MIT](LICENSE).
