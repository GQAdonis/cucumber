# Documentation boundary repair 1

First attempt exited 0 with zero scenarios and zero steps; this is NOT_EXERCISED,
not passing proof. No production site build occurred. Cause from installed
Cucumber.js13.3 configuration loader: an ESM default export is itself the default
profile, so nesting another default object discarded the intended paths/imports.

Repair: export the profile directly. Add a boundary launcher that requires nine
started and finished scenarios, actual successful run completion and exit0.
No production site behavior or feature scenarios changed. Original logs retained.
The complete same nine-scenario boundary will now run; no unit tests.
