# Contribution readiness acceptance

This support code implements the adopted Phase47 boundary. It does not replace
existing Makefile or CI jobs. No component is a unit-test suite or preflight.
The preparation command and both tagged outer BDD commands form one complete
phase-end packet. The owner-bound contract controls its scope and budget.

`prepare.py` exclusively creates `READINESS47_EVIDENCE`, preserves prior ignored
lockfiles, resolves locks, copies the finished source into owned temporary
consumers, extracts immutable Git snapshots, and installs the four pinned oracle
boundaries. It records actual tool versions. Rust1.88.0, Node26.5.0 and
CPython3.11.3 are the local consumer identities. The nightly resolver is pinned
to nightly-2026-11-18 and its observed compiler commit, not an ambient nightly.
Rust1.100.0 is acquired only for the historical book comparison. Preparation is
part of acceptance; invoking it during implementation is forbidden.

`READINESS47_CONTRACT_DIGEST` must be supplied from the current supported KBD
binding after the implementation-complete amendment. The driver compares it to
the adopted artifact and retains it in runtime and case receipts. It does not
accept the earlier specification digest as an implicit current binding.

The Rust harness selects exactly ten scenarios for each tag and writes actual
source-aware Messages beside normal text summaries. The driver invokes only
named existing `harness=false` BDD targets. It does not invoke a workspace/unit
suite, doctests, lint, `cargo check` or a standalone typecheck. Compiling and
launching the real external consumer is part of the behavior it proves.

The 49 affected Cucumber targets and standalone parser run once in the fresh
packet. Cases that need the same result reference its retained, scoped process
receipt rather than rerun it or reuse historical logs. Case10 additionally
prepares and executes both installed SDK packets. The explicit successor map
permits only three changed local acceptance source hashes; predecessor official
fixtures, locks and licenses remain unchanged. The old Phase46 identity artifact
is never edited, and this evidence is Phase47 rather than retroactive Phase46
certification.

The book fixture preserves the immutable introduction's Rust block, hidden setup
and Gherkin feature. Base/head applications execute under Rust1.88 and1.100;
actual Cargo artifact paths are retained. This is not a reproduction or waiver
of the unchanged remote mdBook job, and the driver records its causality UNKNOWN.

After the controls, `finalize.py` requires twenty actual completed outer cases,
sixty passed steps, all current child receipts, the installed SDK proof, and
unchanged original source hashes. It removes only the marked temporary root.
Failures retain consumers and original logs. Original Git snapshots, locks,
package/native identities, diagnostics, receipts and Messages remain evidence.
Registry operations, deployment, workflow changes, unsupported generic inventory,
foreign step execution and framework parity are not claimed here.
