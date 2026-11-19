---
id: evidence
title: Evidence
---

# Evidence

The preserved foundation is verified through phase45 using focused BDD acceptance at completed phase boundaries. Features preceded implementation. These results do not certify proposed SDK/native bindings, this documentation site, or complete ecosystem parity.

| Completed boundary | Passed scenarios / steps | Retained evidence |
| --- | --- | --- |
| Phases43–45: receipt consistency, rerun and Markdown precedence, including prior VLBV cases | 87 / 348 | [Original primary log](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/evidence/phase43-45-first-bdd.log) |
| Eight affected root targets | 106 / 460 | [Affected log](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/evidence/phase43-45-affected-bdd.log) |
| Rust1.88 selected delivery acceptance, 13 targets | 172 / 670 | [MSRV log](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/evidence/msrv-1.88-first-bdd.log) |
| Sibling parser affected acceptance | 73 / 241 | [Parser log](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/evidence/phase45-parser-affected-bdd.log) |

These are separate runs with overlapping scenarios; adding their counts would not give a unique coverage total. The [exact phase43–45 commands](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/evidence/phase43-45-commands.txt) and [historical phase record](https://github.com/GQAdonis/cucumber/blob/6e4753fc0783038bb388de1b4d76055edc697b8f/docs/compatibility/LIVE-STATUS.md) retain scope and diagnostics. Initial failures and zero-selection mistakes remain recorded and are excluded from passing evidence.

The implementation was preserved in Cucumber commit [6e4753f](https://github.com/GQAdonis/cucumber/commit/6e4753fc0783038bb388de1b4d76055edc697b8f) and Gherkin commit [efb91e8](https://github.com/GQAdonis/gherkin/commit/efb91e8bb5a7d59a717f88c05d1c06ec5d06a819), on `foundation/rust-bdd-sdk`. This does not represent a registry release or deployment.

A complete independent post-implementation audit remains a gate before upstream contributions. No clean-code or canonical KBD certification is claimed. Read the [compatibility boundaries](./compatibility.md) alongside the results.
