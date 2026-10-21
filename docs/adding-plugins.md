# Adding plugins

Copy the starter as a working package:

```sh
cp -R plugins/repo-inspector plugins/my-plugin
```

1. Update `name`, `version`, `description`, and `keywords` in `plugin.json` and
   `.claude-plugin/plugin.json`. Optional `author` and `license` fields must also
   match when present. Keep those fields identical.
   Use a lowercase kebab-case name matching the directory and a version such as
   `1.0.0`. This starter validator accepts stable `MAJOR.MINOR.PATCH` versions.
2. Update `extensions.com.openai.interface` in the portable manifest for the
   Codex listing. Describe the actual workflow and supply useful default prompts.
   Choose a broad [supported category](https://developers.openai.com/plugins/deploy/submission-errors#listing-and-interface-errors),
   such as `Developer Tools` for coding workflows or `Productivity` for planning
   and documentation. Use specific workflow keywords in both plugin manifests.
3. Replace `skills/repo-map/` with your skills. Each skill belongs in
   `skills/<skill-name>/SKILL.md` and starts with YAML frontmatter containing
   `name` and `description`. Use an unquoted name and a single-line description,
   either plain text or a JSON double-quoted string. Quote descriptions that
   contain YAML punctuation such as a colon followed by a space. The lightweight
   validator checks this subset; it is not a complete YAML parser.
4. Write the plugin README with invocation examples, expected output, runtime
   dependencies, and any credentials or side effects.
5. Add the plugin to both catalogs with source `./plugins/my-plugin`. In the
   Codex catalog, use the local source object and an `AVAILABLE` installation
   policy. Copy its authentication policy for skills-only plugins; it causes no
   login without a service connection. Set the same `category` in both catalogs,
   matching the portable manifest's listing category. Keep catalog ordering aligned.
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

For third-party skills, preserve the original author and applicable license
notices. Record the upstream version or commit and document local adaptations.
Use a bundled snapshot so installation does not depend on another marketplace;
include every resource its workflows need after installation.
