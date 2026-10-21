# Third-party notices

This package redistributes the eight skills and icons from the installed
`engineering-suite-ponytail` 2.0.0 plugin in `openai-curated-remote`.
Its manifest credits Saul Martí; its MIT license credits Engineering Suite
contributors. [LICENSE](LICENSE) preserves that notice verbatim.

The third-party skill sources are:

- **DietrichGebert / Ponytail**, commit
  `356918eba965ee1eac64bd3a7f0dd02108350de5`: `ponytail`, `ponytail-review`,
  `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, and `ponytail-help`.
  Source: <https://github.com/DietrichGebert/ponytail>.
  License: [ponytail-LICENSE](third_party_licenses/ponytail-LICENSE).
- **Addy Osmani / Agent Skills**, commit
  `6ca0cd7db39b41b1c37e26d335c507ee92382c6d`: `code-simplification`.
  Source: <https://github.com/addyosmani/agent-skills>.
  License: [addy-LICENSE](third_party_licenses/addy-LICENSE).

The `entry-ponytail` router comes from the Engineering Suite bundle.
[UPSTREAM_LOCK.json](UPSTREAM_LOCK.json) preserves the original skill hashes and
the relevant upstream source records.

## Marketplace adaptations

Arnold Stark maintains these packaging changes:

- Use the local plugin name `ponytail` and package version `1.0.0`; retain the
  upstream bundle version separately in the lock file.
- Add a portable manifest, a matching Claude Code manifest, and marketplace usage
  documentation. Point the Codex icons at their bundled `assets/` paths.
- Adapt `ponytail-help` to the host invocation forms and this marketplace's update
  flow; remove standalone startup-hook configuration instructions.
- Replace the gain skill's missing local benchmark pointer with bundled
  provenance. Correct the historical cost range to match the pinned upstream
  benchmark table, and retain its distinction from per-project savings.

All other skill files and included license texts remain unchanged. No standalone
Ponytail hooks or benchmark executables are bundled.
