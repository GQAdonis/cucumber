# Phase47 boundary plan proposal

Status: specification input only, 2026-11-18. The successor/assessment is authorized; this plan is not an adopted execution contract. No proposed harness below exists merely because it is named here. No build, test, import, lint, schema-validation program or executable probe was run to prepare this document. Source text and retained evidence were read. Internal planner `/root/sdk47_scope`; exact model/deployment UNKNOWN.

This proposal addresses the ten outcomes in `.kbd-orchestrator/phases/phase-47-contribution-readiness/scenario-candidates.md` and the two independent assessment reviews. Foreign execution, Behave/pytest-bdd adapters, registry publication and changes to mature build/release workflows are excluded. Preserve `foundation/rust-bdd-sdk` and Pages deployment source when preparing fork-main contributions.

## Technical design inputs and adoption boundary

1. Resolve exact dependency lower bounds as an implementation/design responsibility from package source/manifests, including the observed jsonschema0.33/idna1.0.2/ICU1.4/zerovec0.10.4/yoke split. A normal graph is not minimal-resolution proof. Do not guess constraints or replace the existing matrix with a newer-lock-only success.
2. Resolve book failure causality against the PR base and exact mdBook0.5.4/Rust1.100.0 incident identities. Retain UNKNOWN until source analysis or an expressly adopted boundary comparison proves attribution. The immutable comparison base is cucumber d95872541ee2a43d71089c64bd3fa8848e24c922; use the actual introduction example from book/src/introduction.md. Bind its bytes before executable authoring. Unknown cause is a bounded diagnostic outcome, not permission for an early probe or a request for the owner to choose a technical fix. Parent source review of mdBook0.5.4 found that its driver resolves relative library search paths against the original process cwd before invoking rustdoc in a temporary directory; therefore a blanket “relative -L breaks in tempdir” explanation is unsupported. Do not prescribe an absolute-path Makefile fix without actual cause evidence. Inspect resolved artifact names/search paths/tool identities and compare the immutable base within the adopted BDD boundary. Primary sources: [driver](https://github.com/rust-lang/mdBook/blob/v0.5.4/crates/mdbook-driver/src/mdbook.rs), [CLI](https://github.com/rust-lang/mdBook/blob/v0.5.4/src/cmd/test.rs). There is no permission here to alter the Makefile's `make test.book` implementation or workflow.
3. Pin the nightly Cargo resolver identity to the observed rustc1.102.0-nightly commit59cbdee2e (2026-11-17) and record Cargo identity at the authorized boundary; select the matching dated toolchain from official distribution metadata before implementation. This is an implementer responsibility, not an owner preference. Preserve the exact resolver identity for the existing `-Z minimal-versions` operation, and the immutable baseline commit/fixture hashes for comparisons. Rust1.88.0 remains the consumer compiler. Resolve dependency and fixture acquisition prerequisites before implementation; acquisition/install/build execution is dormant until the phase boundary.
4. Review the static counts below against the final source inventory and bind them in the adopted contract. Proposed new scenarios are ten functional cases and ten separate controls, each with Given/When/Then:20 scenarios/60 outer steps. Existing inventories must not silently grow to absorb a new defect. Changed scope requires the established amendment route.
5. Register all required lifecycle stages, including Reflect, before closure using supported commands. Record owner calibration honestly; successor signing is not ten invented per-case verdicts.

## Proposed new acceptance entry point and evidence

Author `tests/features/contribution_readiness/readiness.feature` and `tests/contribution_readiness.rs` first. Proposed Cargo entry: `[[test]] name = "contribution_readiness"; harness = false; required-features = ["macros", "output-messages"]`. Add an evidence driver under `tests/readiness/` only as acceptance support, leaving existing Makefile/workflows intact. A new exact tag pair, `@readiness47` and `@readiness47_negative`, selects exactly10 scenarios/30 steps per command. The driver exclusively creates a fresh `READINESS47_EVIDENCE` directory; source-aware outer Messages, raw child stdout/stderr, argv/cwd/env allowlist, exit statuses, fixture/lock/native artifact hashes, timestamps, oracle identities, counts and cleanup receipts are mandatory. A zero/partial/skipped outer selection is FAIL, not a green exit. Negative controls must prove rejection without mutating real sources or original evidence.

Proposed whole-phase commands (NOT executable authorization and NOT present today):

```sh
READINESS47_EVIDENCE=/fresh/absolute/phase47-packet RUSTUP_TOOLCHAIN=1.88.0 python3 tests/readiness/prepare.py
env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --all-features --test contribution_readiness -- --tags @readiness47
env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --all-features --test contribution_readiness -- --tags @readiness47_negative
```

The preparation operation must be part of the single complete boundary packet, never a preliminary check. It owns fresh external consumer directories and locked oracle installation. It must not invoke local unit suites, `cargo test --workspace`, `make test.cargo`, `make cargo.lint`, standalone lint/typecheck suites or mdBook doctests. The functional/control cases may compile and launch the actual consumer whose behavior they specify; that is artifact acceptance, not a renamed generic test suite.

## Ten cases and independent controls

| ID | Real operation and independent oracle | Control / exact acceptance obligation |
| --- | --- | --- |
| CR47-001 | Same original Examples source containing `| \     |` and a step-table counterpart through `GherkinEnv::default()`, `new("en")`, `new_latest("en")`, and explicit `TableSemantics::Gherkin43`; compare legacy expectation at immutable upstream base and explicit43 results with pinned official Gherkin43. Include recognized escaped newline/pipe/backslash and the following step. | Default/new/new_latest retain legacy rejection; latest vocabulary alone cannot opt into43 table semantics. Switching only the table policy must change the relevant result. Existing six literal-escape cases select explicit43 intentionally; do not delete argument-order behavior. |
| CR47-002 | External consumer pattern-matches unchanged public `ParseFileError` variants/fields and records classic diagnostic, structured line/column and path, additive Markdown error, then valid parse. Oracle is retained pre-change public observations/source, not an error string manufactured by the revised parser. | A mutated path/location or missing error must be rejected. Keep ordinary error text comparisons canonical only where the public contract promises it (expected-token sets need stable normalization). Private representation changes cannot alter variant signatures or swallow errors. |
| CR47-003 | Compare parser fork/vendor production identity and run the same legacy/43, featureless and malformed cases through separate external consumers linked to each source. Inventory `src/**`, `build.rs`, included generated/input files and both manifests, with explicit documented packaging-only manifest differences. Retain each git/source hash and actual loaded dependency path. | Change one byte only in a disposable comparison copy and prove the checker rejects it. Also corrupt one behavioral observation. Never edit the actual vendor to manufacture a passing control. The two implementations alone are not an independent semantics oracle: retain CR47-001 official/base comparisons. |
| CR47-004 | Fresh external applications compile and execute meaningful matched and undefined scenarios with `default-features=false`, separately with: none, macros, timestamps, output-json, output-junit, libtest, tracing, and output-messages. These are eight explicit profiles. Child compile/run uses `RUSTFLAGS=-Dwarnings`, Rust1.88 and the accepted graph. Hand-register a World/step when macros is absent. | Every positive fixture records a handler side effect and appropriate enabled output; an undefined step must produce a real failure/undefined result without that side effect. No-Messages warnings are not hidden by enabling all features. This is actual consumer execution, not standalone cargo-check evidence. |
| CR47-005 | External BDD consumers use a generic World and custom initializer, exercising generated DefinitionOptions, explicit timeout/metadata where supported, attachment and completion context access; ordinary legacy World remains usable. Compare actual lifecycle/handler/attachment traces with declared business outcomes and core writer Messages. | Deliberately remove expected definition metadata or misassociate attachment scope and require rejection. Existing codegen unit expectations may be corrected to the intended token structure, but their local execution is excluded; real consumer behavior is the local acceptance oracle. |
| CR47-006 | Run existing dry_run acceptance from a clean oracle install, through the actual `tests/interop/consume.mjs` and `scenario-hooks.mjs` child processes. Retain pinned `@cucumber/query16.0.0`/Messages34.2.1 identities and real returned outcomes. | Remove the package only in a disposable install and launch a fresh process. Missing oracle must visibly fail; no skip, canned response or lookup from the developer's node_modules. Exact command failure is expected control evidence, not acceptance success by itself. |
| CR47-007 | In isolated copied source/consumer workspaces, resolve minimum dependencies with pinned nightly `cargo update -Z minimal-versions`, retain resulting locks and dependency identities, then use Rust1.88 to compile AND execute the actual affected consumer path. Include the root/dev-dependent schema-validation path that exposed jsonschema/ICU failure; a consumer-only graph omitting dev dependencies is insufficient. | Preserve the recorded incompatible graph as the rejected control, including the actual distinct yoke identities. A normal compatible-latest lock cannot satisfy this case. Bind the recorded incompatible graph and failure semantics before generation. The implementer selects corrected lower bounds from source evidence within the adopted design/implementation scope; unresolved correction yields an honest B4 BLOCKED/FAIL. No early probe or owner dependency-version choice is required. |
| CR47-008 | Extract the agreed immutable book example into an external application, build/link/run it under the real BDD case, and assert its actual step execution/results. Preserve source-block identity and any documented hidden lines/setup. Compare PR/base snapshots with the same toolchain/layout where the accepted cause investigation requires it. | Remove a required dependency only in the disposable consumer; linking/execution must fail. An existing `.rlib` file is not proof. Local `make test.book` is excluded because it executes mdBook doctests; the unchanged remote `test-book` matrix remains an additional gate. A passing surrogate example cannot certify the remote Makefile path. |
| CR47-009 | Invoke each adopted BDD entry point at its intended dedicated feature path; retain exact selected scenario/step identities and final Messages/nonzero receipt. For Gherkin use its dedicated `step_arguments` acceptance, preserving the historical `tests/cucumber.rs` semantics (no registered steps, intentional skips). | Wrong tag/empty feature directory must fail in the NEW boundary guard. Do not impose fail-on-skipped on the legacy empty-step harness merely to make this new case pass. Preserve packaging inclusion if the dedicated compatibility feature path changes. |
| CR47-010 | Execute the fixed affected packet below plus actual installed native SDK preparation/functional/control packets. Shared parser/source/Markdown, matching, hooks, Messages, rerun and installed-package outputs retain their independent official corpus, JS consumers and earlier acceptance obligations. | Existing negative controls must execute, not merely be listed. Reject fixture/source hash changes, dropped attempts or native-library removal where existing controls specify them. No earlier phase log is substituted for this changed-source run. No full-language/framework/platform parity inference. |

The eight CR47-004 profiles include the seven existing remote feature entries (none plus macros, timestamps, output-json, output-junit, libtest and tracing) and an explicit output-messages profile; the precise list above is authoritative. Each profile needs its actual applicable public API and output assertion fixed in the scenario fixture before adoption; unsupported combinations must not silently become skips.

## Existing reusable BDD packet

All listed targets exist today and declare `harness = false`. Commands run from the Cucumber root, at phase end only, using one explicit target per recorded invocation:

```sh
env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --all-features --test TARGET
```

`TARGET` is replaced once by each name in the table below, not by `--tests`, `--workspace` or a wildcard. Existing `tracing`/`wait` demonstrations and Rust unit/json/junit/libtest harnesses are not added to this local packet. The table is a proposed broad affected packet because formatting/codegen/feature gating touch shared delivered source. An owner-adopted narrower set requires an explicit source-to-case rationale, not silent omission.

The following counts were read from feature source text, expanding Examples rows and ignoring doc-string contents; they are planning inventory, NOT runtime results or independent proof. Their scenario names/rows and source hashes must be frozen before generation. If source structure invalidates this inventory, resolve it before adoption, not by silently accepting a different count at runtime.

| Existing target | Planned scenarios | Planned steps |
| --- | ---: | ---: |
| `compatibility` | 20 | 115 |
| `portability` | 1 | 5 |
| `hooks` | 9 | 42 |
| `messages` | 20 | 97 |
| `scheduling` | 8 | 50 |
| `sources` | 21 | 81 |
| `messages_source` | 19 | 80 |
| `messages_retries` | 6 | 40 |
| `messages_hooks` | 10 | 70 |
| `messages_consumer` | 2 | 8 |
| `messages_docstrings` | 15 | 86 |
| `interpolation` | 9 | 41 |
| `messages_errors` | 6 | 30 |
| `messages_backgrounds` | 12 | 64 |
| `messages_logs` | 7 | 46 |
| `messages_versions` | 3 | 12 |
| `step_hooks` | 10 | 51 |
| `expression_compat` | 53 | 159 |
| `messages_corpus` | 62 | 236 |
| `messages_attachments` | 9 | 36 |
| `messages_documents` | 11 | 41 |
| `run_hooks` | 14 | 62 |
| `scenario_hook_records` | 18 | 76 |
| `messages_support_code` | 14 | 56 |
| `messages_run_hooks` | 6 | 34 |
| `messages_markdown` | 21 | 78 |
| `messages_markdown_runtime` | 14 | 54 |
| `messages_scenario_hooks` | 13 | 64 |
| `messages_expression_metadata` | 19 | 85 |
| `timeouts` | 14 | 50 |
| `execution_control_formats` | 18 | 54 |
| `composable_filters` | 12 | 56 |
| `execution_control` | 20 | 87 |
| `dry_run` | 14 | 59 |
| `line_selection` | 38 | 178 |
| `messages_custom_metadata` | 16 | 78 |
| `dry_run_formats` | 9 | 30 |
| `retry_policy` | 16 | 56 |
| `ordered_scheduling` | 19 | 81 |
| `lexical_semantics` | 25 | 110 |
| `vlbv_adapter` | 47 | 175 |
| `source_paths` | 13 | 44 |
| `dynamic_assignment` | 14 | 55 |
| `messages_table_columns` | 11 | 53 |
| `timeout_preparation` | 17 | 69 |
| `expression_names` | 12 | 47 |
| `generated_ordering` | 10 | 45 |
| `messages_rerun` | 19 | 73 |
| `messages_markdown_precedence` | 21 | 100 |
| **Total: 49 targets** | **797** | **3399** |

Gherkin fork command, from its own root:

```sh
env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --test step_arguments
```

Historical dedicated-parser baseline:73 scenarios/241 steps; freeze its current cases and the agreed policy-only correction. Do not use the old `--test cucumber` empty-step harness as evidence that compatibility scenarios executed. The Cucumber consumer targets above explicitly cover Document/Markdown/lexical/source/AST/Pickle behavior absent from the standalone parser harness. Fork/vendor correspondence is separately exercised by CR47-003.

Reuse the existing SDK46 installed-artifact packet in a fresh phase47 evidence directory, with the already-adopted host identities (Darwin arm64, Rust1.88.0, Node26.5.0, CPython3.11.3, TypeScript6.0.3). Do not reuse old runtime.json or existing external installations:

```sh
export PATH=/Users/gqadonis/.local/share/fnm/node-versions/v26.5.0/installation/bin:$PATH
SDK46_EVIDENCE=/fresh/absolute/phase47-sdk RUSTUP_TOOLCHAIN=1.88.0 /Users/gqadonis/.pyenv/versions/3.11.3/bin/python3 sdk/acceptance/prepare.py
env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --manifest-path sdk/Cargo.toml --test language_sdk -- --tags @sdk46
env RUSTUP_TOOLCHAIN=1.88.0 cargo test --locked --manifest-path sdk/Cargo.toml --test language_sdk -- --tags @sdk46_negative
```

Both harness commands must inherit the same exact Node PATH/runtime identity as preparation. Existing packet expectation:11/33 functional plus11/33 controls, outer Messages22/66, installed native realpaths/hashes and owned cleanup. These machine paths identify this host boundary, not portable packaging instructions. This is a newly adopted rerun under phase47, not an extension of exhausted phase46 authority. Copies of native artifacts remain ignored, while identities/receipts are retained.

## Locked collaborator inventory and preparation

Install every selected oracle into a fresh owned acceptance root at the complete boundary, using the exact retained package.json/package-lock.json pair and `npm ci --ignore-scripts --no-audit --no-fund --prefix DIRECTORY`. Placement must let each existing script resolve its own package boundary without NODE_PATH fallback; acceptance source changes must make this repeatable under the unchanged CI entry point too. A network/cache failure is BLOCKED or FAIL with original exit/log, never skipped proof. Do not invent a package-install workflow step or rely on ambient node_modules to evade the packaging defect.

| Existing package boundary | Locked direct oracle packages | Used for |
| --- | --- | --- |
| `tests/interop` | @cucumber/query16.0.0, @cucumber/messages34.2.1, @cucumber/junit-xml-formatter0.15.0 | dry-run, Messages consumers, hooks, attachments/logs, schema/protocol consumers |
| `tests/interop/gherkin43` | @cucumber/gherkin43.0.0, @cucumber/messages35.0.0 | official plaintext/Markdown/source graph and lexical fixtures |
| `tests/interop/expressions` | @cucumber/cucumber-expressions20.1.0, @cucumber/tag-expressions11.0.1 | expression/name/capture/tag comparisons |
| `tests/interop/rerun` | @cucumber/cucumber13.3.0 | actual rerun formatter/collector |

SDK preparation owns its additional exact native/tool/declaration packages and external consumers as already recorded in `sdk/acceptance/prepare.py`; retain that function's generated graph/native/command provenance. Node executable/version and npm identity must be recorded, not inferred from a shell-manager setting. Offline replay is not claimed unless the accepted cache is complete and every original collaborator actually executes. No new package registration/publication is involved.

## Separate unchanged remote checks and publication decisions

Keep all original `.github/workflows/ci.yml` and Makefile requirements. Local BDD success permits the authorized preservation push; it does not itself mark a PR ready or permit merging. Existing PR pushes then automatically run remote formatting/clippy/feature/minimum/MSRV/test/book/rustdoc checks. Some are unit suites: label them honestly as remote unchanged CI, never local BDD. Do not run them locally or relabel `make test.book` as BDD.

Cucumber remote requirements: `pr` aggregate; clippy; rustfmt; seven feature entries (`<none>`, macros, timestamps, output-json, output-junit, libtest, tracing); Rust1.88 MSRV for cucumber and cucumber-codegen on Ubuntu/macOS/Windows; stable/beta/nightly test matrix for both crates on those three OSes; test-book on all three OSes; nightly rustdoc for both crates. Gherkin: `pr`; clippy/rustfmt; four feature entries (`<none>`, parser, serde, juniper); Rust1.88 MSRV on three OSes; stable/beta/nightly tests on three OSes. These counts describe workflow source, not green results. Retain actual head SHA, run/job/check conclusion, base SHA and mergeability; absent checks are not PASS. Release/tag jobs are outside this phase and must not be triggered.

The Cucumber main workflow also contains the existing mdBook deployment job: it writes book output to gh-pages with keep_files:true. Pages is configured for workflow-based Docusaurus deployment, not branch publication. Preserve both existing workflows and the foundation Pages source branch; do not invent a hosting-approval gate or claim a main-branch deployment was already exercised. Confirm actual post-merge delivery state as part of the authorized readiness work.

An upstream draft with no checks cannot be promoted based on an empty check list. Existing upstream contribution rules, overlap and dependencies still apply; no upstream merge/issue closure or registry operation is authorized by this plan.

## Finite budget, stopping and review

Proposed cumulative budget:300 elapsed minutes,200 tool calls, at most2 repairs, no-progress threshold3. Count from the eventual adopted execution dispatch, including preparation, execution, review, authorized repair and remote waiting unless the owner explicitly adopts a different accounting rule. No invented resets, excluded waiting or exact telemetry claims. Each repair needs its established authorization and a fresh retained boundary packet; no opportunistic isolated test/debug runs between production edits.

**Budget mismatch risk:**49 root targets plus standalone parser, installed native packages, eight feature consumers, minimal-graph/book comparisons and OS/remote matrices may exceed300 minutes on cold caches or queue delays. This is a proposal, not a runtime estimate or completion promise. If the actual bound is exhausted, stop dependent execution and report retained status; do not weaken checks or claim local proof equals merge readiness. Before adoption the parent may split source repair/local proof from remote readiness into explicit phases, with genuine handoff/authority and no hidden continuation.

After successful whole-phase behavior and actual required remote checks, independent internal reviewers audit the complete delivered Cucumber/Gherkin diff (not just phase47 fixes), including Rust SDK/FFI/wrappers, compatibility/defaults, ownership/error handling, maintainability, documentation and packaging boundaries. Retain reviewer IDs, exact model UNKNOWN when unavailable, findings/dispositions and source digests. No external reviewer transmission. Material behavioral findings consume the adopted repair allowance and complete affected BDD boundary; unresolved findings block readiness/merge. Review does not certify unimplemented foreign execution or public package distribution. Reflect is registered before closure and completed through supported KBD lifecycle; no direct canonical edits.

## Remaining adoption decisions

- Owner decision is the finite acceptance scope/budget and local-versus-remote verification boundary. Dependency constraints, toolchain artifact selection and book diagnosis are implementation/design responsibilities within that scope; unknowns remain explicit and may not justify early execution or process changes.
- Approve or reduce with rationale the fixed49-target affected packet, eight consumer profiles and10+10 new scenarios; accept300min/200calls/2repairs only with the cold-cache/remote-queue risk explicit.
- Confirm the local-BDD versus unchanged automatic remote-unit/lint/book policy and whether remote wait belongs in this same finite phase or a distinct ready/merge gate.
- Binding the reviewed case contract remains necessary. The prior signed successor authorizes phase entry only; no per-case owner verdict is invented here.
