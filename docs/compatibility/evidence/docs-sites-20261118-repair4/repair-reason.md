# Documentation boundary repair 4

Both production builds succeeded. Nine scenarios executed, but only three passed.
Original 56-step results, screenshots, browser observations and failures remain.

Three harness defects are corrected together before another full boundary:
- footer matched both article and global footer; use the contentinfo landmark.
- mobile navigation selected an inert offscreen primary-menu link; select the
  active non-inert panel and prove actual focus before pressing Enter.
- negative copies sharing node_modules failed SSR for unrelated metadata, so
  neither failure was admitted as broken-link proof. Each copy now gets its own
  npm ci installation and must first pass an unmodified production build before
  the broken-link mutation. Preserve install/baseline/control logs separately.

No site source, scenario contract or acceptance oracle is weakened. Original
source/build identities remain compared after controls; cleanup remains required.
