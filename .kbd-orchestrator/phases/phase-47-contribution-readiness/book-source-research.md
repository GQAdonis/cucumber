# Book failure source research — no execution

Observed CI uses Rust1.100.0 and mdBook0.5.4; cargo build succeeds, subsequent book rustdoc reports E0463. Cause remains UNKNOWN.

Primary source inspected: https://github.com/rust-lang/mdBook/blob/v0.5.4/crates/mdbook-driver/src/mdbook.rs (test_chapter, lines235 onward), https://github.com/rust-lang/mdBook/blob/v0.5.4/src/cmd/test.rs and driver load.rs. test_chapter captures process cwd and converts relative -L inputs to absolute paths before starting rustdoc in its temporary directory. CLI and load paths inspected do not change cwd. Thus merely changing -L to an absolute path is not established as a fix. Official CLI docs illustrate the same `mdbook test my-book -L target/debug/deps/` pattern our Makefile uses.

At the adopted full boundary, record actual toolchain identity, compiler artifact paths and meaningful book-code consumer behavior, with a pinned upstream-base comparison where required. Local `make test.book` runs a doctest suite and is not permitted to masquerade as BDD. Existing remote CI remains distinct. Do not remove or change its gate based on this unconfirmed hypothesis.
