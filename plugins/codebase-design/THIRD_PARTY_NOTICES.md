# Third-party notices

This package redistributes all four skills, their referenced resources, and icons
from `engineering-suite-codebase-design` 2.0.0 in `openai-curated-remote`.
Its manifest credits Saul Martí; its MIT license credits Engineering Suite
contributors. [LICENSE](LICENSE) preserves that notice verbatim.

The architecture-review skill also calls `grilling` and `domain-modeling`.
Those dependencies, their UI metadata, and the domain-modeling formats are
included from `engineering-suite-grill-me` 2.0.0 so this package is self-contained.

All five non-router skills come from **Matt Pocock / AI Hero skills**, commit
`3cca18b368ae95cdbdebbff572ccafa662551015`:

- `codebase-design`
- `improve-codebase-architecture`
- `setup-ts-deep-modules`
- `grilling`
- `domain-modeling`

Source: <https://github.com/mattpocock/skills>.
License: [aihero-LICENSE](third_party_licenses/aihero-LICENSE).
The `entry-codebase-design` router and icons come from Engineering Suite.

[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) records both source bundles, the shared
upstream commit, and original hashes of all copied files.

## Marketplace adaptations

Arnold Stark maintains these packaging changes:

- Use the local name `codebase-design` and an independent package version,
  starting at `1.0.0`; retain upstream bundle versions `2.0.0` in the lock file.
- Add matching portable and Claude Code manifests, usage documentation, and a
  Developer Tools listing. Point Codex icons at their bundled `assets/` paths.
- Include the two missing interview dependencies and their supporting files
  within the package, preserving their original invocation policies.
- Link bundled workflows from the entry skill and replace architecture-review
  and TypeScript-setup `Skill` tool calls with links to local skill files that
  either client can load.

Other workflow instructions, supporting documents, configuration, UI metadata,
icons, and license texts are preserved.
