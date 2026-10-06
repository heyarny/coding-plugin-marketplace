# Publishing to GitHub

The local catalogs already use repository-relative sources. Publishing does not
require changing their paths.

## First publication

Choose the GitHub owner, repository visibility, marketplace title, publisher
name, and license before publishing. The starter uses `coding-plugins-marketplace`,
publisher `Arnold`, and MIT. Update the manifests, catalogs, and LICENSE if needed.
Run the two checks in the root README and review `git diff --cached` before
committing. If you have no commit yet:

```sh
git add .
git commit -m "chore: initialize coding plugins marketplace"
```

After authenticating with GitHub CLI, replace `OWNER` below with your account or
organization. Use `--private` instead of `--public` for private distribution.

```sh
gh auth login
gh repo create OWNER/coding-plugins-marketplace --public --source=. --remote=origin --push
```

If the GitHub repository already exists, add its URL as `origin` and push the
current branch instead. Keep `main` as the default branch.

Once the repository exists, add its real `repository` and `homepage` URLs to
both plugin manifests. Enable GitHub private vulnerability reporting. Require
the `validate` CI check and pull-request review on `main` using a ruleset where
your account plan supports it. Allow Dependabot's action updates after review.

## Install from GitHub

Replace `OWNER` with the published owner.

```sh
# Codex CLI
codex plugin marketplace add OWNER/coding-plugins-marketplace
codex plugin add repo-inspector@coding-plugins-marketplace

# Claude Code
claude plugin marketplace add OWNER/coding-plugins-marketplace
claude plugin install repo-inspector@coding-plugins-marketplace
```

Start a new session after installation. Use a Git repository source rather than
a raw `marketplace.json` URL: the local plugin paths need the rest of the checkout.
Private repositories require the user's Git credentials and repository access.

## Releases

Bump both manifests for every shipped change to a plugin. Test installations
from the repository, then tag the reviewed commit. For the starter plugin:

```sh
git tag -a repo-inspector-v1.0.0 -m "Release Repo Inspector 1.0.0"
git push origin repo-inspector-v1.0.0
gh release create repo-inspector-v1.0.0 --title "Repo Inspector 1.0.0" --generate-notes
```

Tags preserve release history; installations from the default branch follow its
catalog. Pin a marketplace Git ref when consumers need a fixed snapshot.
Submission to the [OpenAI public directory](https://developers.openai.com/plugins/deploy/submission)
or [Anthropic's directory](https://code.claude.com/docs/en/plugins/publish)
is separate from hosting this marketplace on GitHub.
