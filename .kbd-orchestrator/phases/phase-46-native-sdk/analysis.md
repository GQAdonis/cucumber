# Proposed architecture and build-versus-adopt analysis

Independent source research is recorded in library-candidates.json. No candidate
was installed, resolved or built during analysis.

Use a safe sdk/ Rust crate depending on existing cucumber and thin NAPI-RS/PyO3
cdylibs in bindings/node and bindings/python. Each has a separate workspace and
lockfile. Reuse the same Rust implementation; the user did not require one
identical physical shared object. No ABI unsafe code enters core lib.rs.

The first proposed surface is versioned compile-source and rerun operations plus
explicit namespaced Rust Extension dispatch. Inputs/results are owned; core
references never cross the ABI. SourceGraph and Collector remain sole semantic
implementations. Private npm packages include native binary+JS/declarations;
wheels include extension+Python facade. Source distributions require separate
proof of complete Rust path-dependency closure before claiming publication-ready.

Dynamic callbacks follow as real work: Node owns originating-environment dispatch
and Promise completion; Python owns GIL/event loop/context. Do not force Send onto
LocalBoxFuture. Exact handler identity and WorldFactory require additive seams.
Rust timeouts reject late results, but cannot forcibly terminate foreign effects.

Node-API stability differs from CLI/runtime support. PyO3 abi3 does not certify
free-threaded Python. One Darwin arm64 run cannot establish other platforms.
Primary docs: https://nodejs.org/api/n-api.html ;
https://napi.rs/docs/concepts/threadsafe-function ;
https://github.com/PyO3/pyo3/blob/v0.30.1/guide/src/building-and-distribution.md ;
https://github.com/PyO3/maturin/blob/v1.12.6/guide/src/project_layout.md .

Docs references supplied by main conversation:
https://github.com/cucumber/website/blob/main/src/css/custom.scss (greens
#00a818/#39b54a,Lato) and
https://github.com/cucumber/website/blob/main/static/img/logo.svg .
MIT source licensing is not blanket trademark permission. Fork sites must not
imply endorsement; the default mdBook favicon is not a Rust-specific project logo.
