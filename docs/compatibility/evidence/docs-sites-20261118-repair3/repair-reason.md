# Documentation boundary repair 3

Explicit commonjs also rejected generated ESM routes in the preceding real
production build. Nothing reached browser acceptance. All failure logs remain.

The upstream maintainer answer in discussion #11326 explicitly requires
ambiguous module mode, not either forced package type. Remove the type field
from both new site manifests. BDD .mjs remains explicit ESM; configuration is
loaded through Docusaurus. This corrects the previous incomplete package-mode
repair; it does not change scenarios, acceptance criteria or mature workflows.
