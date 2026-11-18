# Phase 47 dependency and oracle implementation notes

Status: implementation written; phase-end behavior proof is pending. No compiler,
installation, test, lint, or import probe was run while preparing these changes.

## Development dependency lower bounds

The retained failing MSRV CI log selects jsonschema 0.33.0, idna 1.0.2,
ICU 1.4, zerovec 0.10.4 and both yoke 0.6.0 and 0.7.3. Registry manifests show
that zerovec 0.10.4 permits `>=0.6.0, <0.8.0`, while ICU provider 1.4 requires
`^0.7.3`. These two yoke versions define different traits.

The development-only `idna = "1.0.3"` and `idna_adapter = "1.2.1"` bounds
move jsonschema's minimum path through the adapter to ICU 2. Its provider uses
`yoke ^0.8.0` and `zerovec ^0.11.1`. Both bounds matter: idna 1.0.2 bypasses the
adapter, and idna 1.0.3 alone allows older adapter implementations. Adapter 1.2.1
has Rust 1.82 as its declared minimum, below this project's Rust 1.88 baseline.
A direct yoke 0.7 dependency would not eliminate an independently selected 0.6.
These are source-level reasons for the change, not a substitute for the adopted
minimum-graph BDD acceptance and negative control.

The exact adopted nightly distribution is `nightly-2026-11-18`. The official
[dated manifest](https://static.rust-lang.org/dist/2026-11-18/channel-rust-nightly.toml)
identifies rustc `1.102.0-nightly (59cbdee2e 2026-11-17)` with full commit
`59cbdee2e7b3ee50e44b460561c43c9e3023d9f0`. The compiler's commit date is one day
before its distribution date. Record actual compiler and Cargo identities when
the approved phase-end packet runs; a directory name does not prove them.

## Official acceptance collaborator preparation

`tests/support/oracle.rs` provides `oracle::command(script)`. It routes the 22
existing package-consuming acceptance callers through a Node-builtins-only
launcher. The four allowed boundaries retain their exact package/lock pairs:

- `interop`
- `interop/expressions`
- `interop/gherkin43`
- `interop/rerun`

A supplied `CUCUMBER_ORACLE_ROOT` is mandatory preparation, never a fallback hint.
The launcher requires `oracle-prepared.json` with `schemaVersion: 1`, canonical
`root`, and `boundaries` entries containing `relative`, `packageJsonSha256`,
`packageLockSha256`, a `scripts` filename-to-SHA256 map, and
`install: {argv: [...], exitCode: 0}`. It compares retained source and mirrored
source/lock hashes and the installed direct package versions. Missing packages,
stale preparation, or an absent explicit root fail the invocation.

Without that environment variable, the unchanged CI entry point prepares an
owned content-addressed root under ignored `target/acceptance-oracles`. A bounded
filesystem lock serializes preparation. Installation invokes npm's JavaScript
entry through the current Node executable, using `ci --ignore-scripts --no-audit
--no-fund --prefix`. No shell parses paths. A failed install retains its original
stdout, stderr, status and command; it cannot produce a successful marker.
`NODE_PATH` and `NODE_OPTIONS` are removed from the oracle launcher environment.
Existing source-tree `tests/interop/node_modules` are not used.

Each invocation retains actual script, lock, installed package paths, Node
identity, argv, working directory, status and captured stdout/stderr in the owned
root's `executions` directory. The oracle's original output and status propagate
to its existing behavior assertion. Phase preparation owns its fresh root and
cleanup; ordinary CI cache artifacts remain ignored. No package locks, mature
workflows or Makefile recipes were changed. The builtins-only VLBV and retained
shuffle implementation fixtures remain direct Node calls.

## Book CI source diagnosis and remaining proof

The failed remote book job uses Rust 1.100 and mdBook 0.5.4. Compilation succeeds,
then every external crate is unresolved with `-L target/debug/deps`. mdBook 0.5.4
already makes that path absolute before its temporary working directory, and
Rust 1.100 forwards library arguments to Markdown doctest compilation.

Cargo's [build cache documentation](https://doc.rust-lang.org/cargo/reference/build-cache.html)
and [layout stabilization](https://github.com/rust-lang/cargo/pull/17354) identify
the intermediate layout change in Cargo 1.100. Artifacts now occupy per-package
hashed directories. This is a strong source-supported explanation for the stale
`target/debug/deps` assumption; base/head phase-end comparison is still required
before claiming runtime causality or an inherited failure.

If that diagnosis is proven, a durable book-runner repair would obtain actual
library parent directories from Cargo's `--message-format=json`
`compiler-artifact.filenames`, instead of assuming either internal layout. This
would touch the established book build recipe, which remains outside this
worker's edit boundary. No absolute-path workaround, toolchain downgrade, or
Makefile/workflow change was made. Local book-consumer BDD is distinct from the
unchanged remote mdBook check; passing the former cannot certify the latter.
