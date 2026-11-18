# Verified pinned JavaScript repeated-capture index discrepancy

Observed at the completed Phase32a BDD boundary, using the untouched installed
`@cucumber/cucumber-expressions` 20.1.0 and its lock-pinned dependency
`regexp-match-indices` 1.0.2. This is a known baseline deviation, not an upstream
fix or a claim that the Rust result matches every pinned JavaScript offset.

Expression: `name {string}`

Actual step text:

```
name "a \"quoted\" word"
```

The nested repeated escape group retains the final value `\" word`. Its actual
UTF-16 range begins at 16. The Rust matcher and independent native JavaScript
`new RegExp(expression.regexp.source, expression.regexp.flags + 'd').exec(text)`
both report 16. The pinned expression library's group reports 8. The BDD checks
that the substring at 16 equals the captured value and the substring at 8 does
not. It compares the full trees and permits only this exact demonstrated nested
start to differ; every other value, position, child and parameter name agrees.

Source evidence from the installed pinned dependency (read, never modified):

- `tests/interop/expressions/node_modules/@cucumber/cucumber-expressions/dist/TreeRegexp.js`
  calls `regexp-match-indices` to obtain capture indices, then constructs its
  argument group tree with `GroupBuilder`.
- `tests/interop/expressions/node_modules/regexp-match-indices/polyfill.js`
  probes `new RegExp("a")` without the `d` flag and selects its implementation
  when that result lacks `.indices`. Modern native `d` support therefore does
  not make this probe select native execution.
- `tests/interop/expressions/node_modules/regexp-match-indices/implementation.js`
  computes starts in `makeIndicesArray` by adding its transformed measurement
  groups to the whole-match start. The observed repeated child keeps the final
  captured value while its computed start corresponds to the earlier repetition.
- `tests/interop/expressions/node_modules/regexp-match-indices/package.json`
  declares version 1.0.2; the existing package lock retains its integrity pin.

Runtime evidence:

- [First boundary: 18/19 passed and the exact mismatch](phase32a-expression-metadata-first-boundary.log)
- [Final boundary: 19/19 and independent native-index evidence passed](phase32a-expression-metadata-bdd.log)

The feature contract was amended before the oracle assertion changed. Installed
packages and production Rust ranges were not altered. The consumer obtains native
indices independently and uses the official library only for the already-compared
group topology. No dependency fork is required merely to reproduce this defect.
