# Live status requested by Travis

2026-11-17. Work is continuing; this is not a final parity claim.

Follow-up phases43–45 passed their first coordinated boundary on Rust1.88:
87 scenarios/348 steps, including25 historical VLBV cases. The new coverage is
22/90 receipt-consistency cases,19/73 native rerun cases and21/100 Markdown
precedence cases. Eight affected BDD targets also passed106/460, including the
relocated external consumer. No compilation or runtime correction was required.
See [the coordinated record](PHASE43-45-BOUNDARY.md).

Since Phase12, completed focused phase-end BDD:

| Phase | Capability | Passed scenarios / steps |
|---|---|---|
| 13 | Docstring edge consistency, native values and official AST/Pickle | 15 / 86 |
| 14 | Official outline interpolation with preserved legacy mode | 9 / 41 |
| 15 | Strict tables through real handlers/errors | 10 / 38; parser73 / 241 accumulated |
| 16 | Empty-scenario background semantics and official empty Pickles | 12 / 64 |
| 17 | Captured-source syntax/expansion/I/O error reporting | 6 / 30 |
| 18 | Exact native case-attempt log Attachments | 5 / 30 |
| 19 | Complete pinned official plaintext corpus | 62 / 236 (50 valid whole AST/Pickle matches;12 invalid rejected) |
| 20 | Ordered per-step hooks and actual invocation records | 10 / 51 |
| 21 | JS-compatible expressions/tags and hygienic macro calls | 53 / 159 |
| 22 | Explicit Messages34.2.1/35.0.0 schemas and unchanged default | 3 / 12 |
| 23 | Typed text/binary attachments and scoped lifetime | 9 / 36 |
| 24 | Global lifecycle setup/gating/cleanup and failure statistics | 14 / 62 |
| 25 | Featureless documents, captured sources and honest empty graphs | 11 / 41 |
| 26 | Actual global-hook definitions/lifecycle and official Query resolution | 6 / 34 |
| 27 | Final support-code registry, actual definitions and matched IDs | 14 / 56 |
| 28a | Native Markdown parser and complete official graphs | 21 / 78; affected92 / 357 regressions |
| 28b | Markdown source policies, immutable capture, handlers and reports | 14 / 54 |
| 29 | Individual scenario-hook observations and evolving cleanup | 18 / 76 |
| 31 | Per-callback Messages, scoped evidence and constructor identity | 13 / 64 |
| 30a | Opt-in per-invocation timeouts, cancellation and cleanup | 14 / 50 |
| 32a | Original builtin expressions, validated captures and parameter descriptors | 19 / 85 |
| 30b | Explicit pending/skipped, scope lifetime, retries and nine built-in consumers | 20 / 87 core; 18 / 54 consumers |
| 33 | Explicit composable names, tags and caller predicates | 12 / 56 |
| 32b | Explicit custom parameter descriptors and raw capture mappings | 16 / 78 |
| 34 | Exact source-line selectors and immutable origins | 38 / 178; without Messages37 / 173 |
| 35 | Dry-run World boundary, honest classifications/lifecycle and consumers | core14 / 59; formats9 / 30 |
| 36 | Validated typed retry budget/tag gating and attempt interoperability | 16 / 56 |
| 37a | Global defined/reverse/exact seeded dispatch, retained retry slots and tracing | native19 / 81; consumers2 / 16 |
| 38 | Explicit official lexical whitespace, source spans/locations and real handlers | 25 / 110 |
| 39 | Read-only VLBV projection, canonical reader, retries and incomplete evidence | 25 / 85 |
| 30c | Explicit owned preparation and callback-factory timing, all hook boundaries | 17 / 69 |
| 37b | Resource-aware assignment, retained reservations, Serial barriers and observations | 14 / 55 |
| 38b | Source-faithful UTF-16 table-cell columns and native values | 11 / 53 |
| 40 | Ordered multi-source discovery, deduplication and Unicode sorting | 13 / 44 |
| 42 | Explicit JavaScript parameter-name admission with real compiler/handler evidence | 12 / 47 |
| 41 | Generated ordering seed observations, reporting and exact replay | 10 / 45 |
| 43 | Lifecycle/retry/process association and all supplied receipt consistency | 22 / 90; existing25 / 85 retained |
| 44 | Native Messages rerun plan, actual JS formatter and exact-row second execution | 19 / 73 |
| 45 | State-aware Markdown tag precedence with official graphs and real handlers | 21 / 100 |

Affected focused BDD regressions also passed. Historical/accumulated cases are
not new coverage. No unit suite, general Cargo test or premature check/build ran.
Initial compilation/harness failures and corrective runs are retained in each
phase's evidence; a shared Phase19 PEG compilation issue temporarily delayed
Phase22 before any of its scenarios executed, then both phases passed.

Current boundary:32b/34/35 completed77 new scenarios/345 steps. Their named
16-target affected BDD batch passed267 scenarios/1115 steps, exit0:
[evidence/phase32b-34-35-affected-bdd.log](evidence/phase32b-34-35-affected-bdd.log).
Phase34 separately passed37/173 with Messages disabled; five existing reporter-only
attachment dead-code warnings were exposed in that configuration. The complete
feature runs had no compiler warnings. Initial harness failures are retained; an
incorrect32b tag selected zero scenarios and is explicitly excluded from evidence.

Latest primary boundary36/37a/38 passed62 scenarios/263 steps. Its named25-target affected
regression passed408 scenarios/1791 steps; sibling parser BDD passed73/241. Initial compile
corrections, a real Unicode preamble failure, its PEG repair diagnostic, and the
retry consumer's final-case/attempt-view correction are retained in the evidence.
No claims about unrun scenarios are based on a successful compiler invocation.

Travis reiterated completion and practical VLBV integration on2026-11-17. Existing
mature build/release processes remain unchanged. Phase39 read-only Messages+receipt
adapter passed25/85, including actual child runner streams and a copied canonical
reader in isolated scratch. Initial incorrect tag selected zero cases and is
excluded; a malformed receipt schema then failed25/25 before repair. All logs remain.
The five-phase primary boundary30c/37b/38b/40/42 passed67 scenarios/268 steps.
Its32-target affected BDD regression passed586 scenarios/2460 steps, exit0.
[evidence/phase30c-37b-38b-40-42-affected-bdd.log](evidence/phase30c-37b-38b-40-42-affected-bdd.log)
retains the results; initial harness-only compiler diagnostics are also retained.
Phase42 additionally retains each actual named child BDD command, compiler
rejection/accepted-handler output and pinned JavaScript registry result.

Phase41 generated-seed observation/replay passed10/45; five affected targets
passed69/282. Final delivery verification passed on `rustc1.88.0`:13 named BDD targets,
172 scenarios/670 steps, exit0. This includes actual relocated and macro consumers.
No MSRV production/dependency fixes were required. See [delivery](DELIVERY.md)
for the local source inventory and exact fork/distribution status. Native async execution is not JS worker-thread isolation;
Rust support-code APIs and regex/numeric semantics retain documented boundaries.

Two upstream inconsistencies are explicitly disclosed: official Markdown's fallback
Feature lacks a keyword required by the Messages schema; pinned JS expression
polyfill reports an incorrect nested repeated-capture start. Native code preserves
official AST fidelity and actual source ranges respectively; full exact parity is
not claimed. The capture deviation has independent native-JavaScript-index evidence.

No access/permission blocker is pending. Through45 implementation and primary
verification are complete; all eight affected root BDD targets passed. No implementation was
committed or pushed; no merge, deployment, production, workflow or security change
occurred. The sole dependency fork remains GQAdonis/gherkin, mirrored in the portable
vendor snapshot; no additional fork has been needed.

Latest sibling parser verification also passed73 scenarios/241 steps on Rust1.88
([evidence](evidence/phase45-parser-affected-bdd.log)). Through42 inventories are
preserved in `evidence/through42-checkpoint/`; current inventories identify the
through45 snapshot. Both repositories remain uncommitted and unpublished.
