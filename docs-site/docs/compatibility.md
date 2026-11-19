---
id: compatibility
title: Compatibility
---

# Compatibility

The GQAdonis fork has bounded, verified interoperability through phase45. It does not claim full Cucumber.js parity or universal Gherkin/Messages conformance.

| Reference | Pinned target |
| --- | --- |
| Native foundation | Cucumber 0.23.0 fork, Rust 1.88 |
| JavaScript runner behavior | Cucumber.js 13.3.0 |
| Official language/compiler | Gherkin 43.0.0 |
| Messages | 34.2.1 default; 35.0.0 explicit |
| JS expression and tag libraries | Expressions 20.1.0; tag expressions 11.0.1 |

Cucumber.js 13.3.0 pins Gherkin 42.0.1 and Messages 34.2.1. The separately adopted Gherkin43 baseline uses Messages35. They are distinct targets, not an assertion that JS13.3 uses the latest parser. See the [version-pinned capability record](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/CAPABILITIES.md#pinned-references).

| Area | Verified boundary |
| --- | --- |
| Language/compiler | Both argument orders, explicit dialect/value/lexical policies, all 62 pinned plaintext fixtures, five official positive Markdown fixture graphs and additional boundaries |
| Execution | Opt-in common step matching; ordered scenario, step and global hooks; retries, timeouts, pending/skipped outcomes and dry-run |
| Protocol | Source-backed AST/Pickle, results, retries, definition metadata and scoped attachments; actual Query16, JUnit0.15 and JS13.3 rerun consumers |
| Selection/scheduling | Typed path/name/tag/line selection, exact-row rerun, seeded ordering, async concurrency and resource-aware assignment |
| VLBV | Read-only deterministic receipt projection, explicit oracle/control/cleanup binding and preservation of failed attempts |

Evidence supports those adopted contracts, not arbitrary formatter plugins or every possible input. See [retained results](./evidence.md).

Known boundaries remain material:

- Official Gherkin43 Markdown fallback AST can omit `Feature.keyword`, while both pinned Messages schemas require it. Source fidelity and universal schema validity conflict for that shape; use an explicit Feature heading when that requirement matters.
- A pinned JS capture-index polyfill returns an incorrect nested repeated-capture offset. Native reporting retains the actual source span rather than reproducing that defect.
- Native async scenarios do not provide JS worker-thread/process isolation or per-worker support-file loading. Rust handlers do not execute JavaScript support files.
- Rust regex syntax, numeric conversions and typed handler transformations remain native. Arbitrary JS plugin/formatter and Python framework compatibility is unverified.
- Dropping an async run does not guarantee cancellation cleanup. The VLBV adapter blocks unsupported stochastic profiles.

The [delivery limits](https://github.com/GQAdonis/cucumber/blob/82c86632d63b323d4c3abdce24c404d0029158d0/docs/compatibility/DELIVERY.md#limits-that-prevent-a-full-parity-claim) and [SDK roadmap](./sdk.md) distinguish protocol interoperability from new language execution bridges.
