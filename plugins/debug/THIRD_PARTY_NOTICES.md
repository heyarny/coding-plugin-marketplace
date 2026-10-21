# Third-party notices

This package redistributes all nine skills, their referenced resources, and icons
from `engineering-suite-debug` 2.0.0 in `openai-curated-remote`.
Its manifest credits Saul Martí; its MIT license credits Engineering Suite
contributors. [LICENSE](LICENSE) preserves that notice verbatim.

Four non-router skills come from **Matt Pocock / AI Hero skills**, commit
`3cca18b368ae95cdbdebbff572ccafa662551015`:

- `codebase-design`
- `diagnosing-bugs`
- `resolving-merge-conflicts`
- `tdd`

Source: <https://github.com/mattpocock/skills>.
License: [aihero-LICENSE](third_party_licenses/aihero-LICENSE).

Four non-router skills come from **Addy Osmani / agent-skills**, commit
`6ca0cd7db39b41b1c37e26d335c507ee92382c6d`:

- `browser-testing-with-devtools`
- `debugging-and-error-recovery`
- `performance-optimization`
- `test-driven-development`

Source: <https://github.com/addyosmani/agent-skills>.
License: [addy-LICENSE](third_party_licenses/addy-LICENSE).
The `entry-debug` router, shared references, and icons come from Engineering Suite.

[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records the source bundle, upstream
commits, and original hashes of all copied files.

## Marketplace adaptations

Arnold Stark maintains these packaging changes:

- Use the local name `debug` and an independent package version, starting at
  `1.0.0`; retain upstream bundle version `2.0.0` in the lock file.
- Add matching portable and Claude Code manifests, usage documentation, and a
  Developer Tools listing. Point Codex icons at bundled `assets/` paths.
- Link the entry skill's bundled workflows and replace TDD's host-specific
  `Skill` call with a local link to the bundled module-design reference.
- Clarify that TDD's reference to a later review stage does not require an
  unbundled `code-review` skill.
- Resolve the reproduction-loop template from its installed skill directory
  and copy/customize it in the target project before execution.
- Add Codex MCP configuration alongside Claude Code's project configuration;
  clarify that the MCP server is a separately configured dependency.

Other workflow instructions, supporting references, helper script, invocation
policies, UI metadata, icons, and license texts are preserved.
