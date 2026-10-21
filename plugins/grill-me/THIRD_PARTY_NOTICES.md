# Third-party notices

This package redistributes all eight skills, their supporting files, and icons
from the installed `engineering-suite-grill-me` 2.0.0 plugin in
`openai-curated-remote`. Its manifest credits Saul Martí; its MIT license credits
Engineering Suite contributors. [LICENSE](LICENSE) preserves that notice verbatim.

The third-party skill sources are:

- **Matt Pocock / AI Hero skills**, commit
  `3cca18b368ae95cdbdebbff572ccafa662551015`: `grill-me`, `grill-with-docs`,
  `grilling`, `domain-modeling`, and `loop-me`.
  Source: <https://github.com/mattpocock/skills>.
  License: [aihero-LICENSE](third_party_licenses/aihero-LICENSE).
- **Addy Osmani / Agent Skills**, commit
  `6ca0cd7db39b41b1c37e26d335c507ee92382c6d`: `idea-refine` and `interview-me`.
  Source: <https://github.com/addyosmani/agent-skills>.
  License: [addy-LICENSE](third_party_licenses/addy-LICENSE).

The `entry-grill-me` router and icons come from the Engineering Suite bundle.
[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records the relevant upstream sources
and original hashes of the files copied into this package.

## Marketplace adaptations

Arnold Stark maintains these packaging changes:

- Use the local plugin name `grill-me` and an independent package version,
  starting at `1.0.0`; preserve source bundle version `2.0.0` in the lock file.
- Add matching portable and Claude Code manifests, usage documentation, and a
  Productivity listing. Point Codex icons at their bundled `assets/` paths.
- Make the router and grilling wrappers resolve bundled workflows through local
  resource links, including when the host has no tool named `Skill`.
- Resolve Loop Me's grilling dependency locally, adapt Idea Refine's question and
  file tool names to the host, and resolve its Bash helper from the installed
  skill while keeping output in the target project.
- Clarify that Interview Me's unbundled downstream workflow names describe
  optional follow-up work, rather than dependencies of the intent interview.

The original skill invocation policies, supporting documents, Bash helper, icon
files, and license texts are preserved. No executable lifecycle hooks are bundled.
