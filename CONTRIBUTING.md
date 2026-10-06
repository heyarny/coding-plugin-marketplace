# Contributing

Keep each plugin focused on one useful workflow. See
[Adding plugins](docs/adding-plugins.md) for the package layout.

1. Create a short-lived branch, for example `codex/add-my-plugin`.
2. Add or update the plugin, its README, and both marketplace catalogs.
3. Keep common metadata identical in both manifests and bump the plugin version
   whenever its shipped content changes.
4. Run the validator and regression tests from the root README. Test the workflow
   in both clients and describe the result in your pull request.

Document dependencies, credentials, file changes, and external actions clearly.
Keep skills self-contained and use relative references to bundled resources.
Introduce MCP servers or hooks only when the workflow needs them; document their
permissions and validate each client's configuration separately.

Use concise Conventional Commit messages such as `feat: add deployment helper`
or `docs: clarify installation`. Submit small, focused pull requests. Third-party
material needs compatible licensing and attribution.
