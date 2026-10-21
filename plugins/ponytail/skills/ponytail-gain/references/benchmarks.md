# Historical benchmark provenance

Source: [Ponytail benchmarks at commit 356918e](https://github.com/DietrichGebert/ponytail/blob/356918eba965ee1eac64bd3a7f0dd02108350de5/benchmarks/README.md),
by DietrichGebert, under the bundled [MIT license](../../../third_party_licenses/ponytail-LICENSE).

Five tasks: email validation, debounce, CSV sum, countdown, and rate limiting.
Three models: Haiku, Sonnet, and Opus. The upstream report uses medians from
single-shot completions, ten runs per cell; cost was rechecked with thirty runs.

| Metric | Arm | Haiku | Sonnet | Opus |
| --- | --- | --- | --- | --- |
| Code lines | Baseline | 518 | 693 | 256 |
| Code lines | Ponytail | 39 | 44 | 51 |
| Cost, USD | Baseline | 0.030 | 0.137 | 0.137 |
| Cost, USD | Ponytail | 0.011 | 0.035 | 0.079 |
| Latency, seconds | Baseline | 37.7 | 124.1 | 58.7 |
| Latency, seconds | Ponytail | 9.9 | 20.1 | 18.0 |

The source reports 80–94% fewer lines, 42–75% lower cost, and 3–6× speed.
These are historical results from June 2026. They are neither predictions nor
measurements for the current project. The upstream honesty note says the bare
baseline includes extra prose/options and overstates the benefit. Multi-turn
agent sessions can have different costs. Use an actual project comparison for
project-specific claims.
