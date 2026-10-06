# Adding plugins

Copy the starter as a working package:

```sh
cp -R plugins/repo-inspector plugins/my-plugin
```

1. Update `name`, `version`, `description`, `author`, `license`, and `keywords`
   in `plugin.json` and `.claude-plugin/plugin.json`. Keep those fields identical.
   Use a lowercase kebab-case name matching the directory and a version such as
   `0.1.0`. This starter validator accepts stable `MAJOR.MINOR.PATCH` versions.
2. Update `extensions.com.openai.interface` in the portable manifest for the
   Codex listing. Describe the actual workflow and supply useful default prompts.
3. Replace `skills/repo-map/` with your skills. Each skill belongs in
   `skills/<skill-name>/SKILL.md` and starts with YAML frontmatter containing
   `name` and `description`. Use unquoted, single-line values for these fields
   in this starter; the lightweight validator checks this convention.
4. Write the plugin README with invocation examples, expected output, runtime
   dependencies, and any credentials or side effects.
5. Add the plugin to both catalogs with source `./plugins/my-plugin`. In the
   Codex catalog, use the local source object and an `AVAILABLE` installation
   policy. Copy its authentication policy for skills-only plugins; it causes no
   login without a service connection. Keep catalog ordering aligned.
6. Run the repository checks. Where Claude Code is installed, also run
   `claude plugin validate .` and `claude plugin validate ./plugins/my-plugin`.
   Install and exercise the workflow in both clients before publishing.

Keep the shared skill instructions vendor-neutral. Put runtime-specific metadata
in the relevant manifest. A copied plugin can only access files packaged inside
its own directory; references to sibling plugins or repository-level docs will
break after installation.

When adding MCP servers, configure the portable package's root `mcp.json` and
Claude Code's `.mcp.json` as each client requires. Hooks and other runtime
components also need explicit compatibility testing. Extend the repository
validator for new component types; its current checks cover skills-only packages.

Use semantic versioning: patches for fixes, minor versions for compatible
features, major versions for breaking workflows. Treat versions as immutable
once published. Keep a changelog with the affected plugin when it starts receiving
releases. Credentials belong in the user's runtime configuration.
