# Documentation boundary repair 2

The first real production build failed in SSR: require.resolveWeak is not a
function. Both webpack bundles compiled, but no page behavior ran. Original
BeforeAll failure/build logs and zero-exercised receipt remain in repair1.

Source cause: marking the site package type=module makes Docusaurus's generated
registry.js an ESM-only webpack module, leaving its require.resolveWeak calls
untransformed. Official upstream discussion #11326 documents the same boundary:
https://github.com/facebook/docusaurus/discussions/11326 .

Repair: use explicit type=commonjs in both new site packages. Docusaurus's
supported ESM config loader still reads export-default config/sidebar files;
BDD .mjs files remain native ESM. No established repository workflow changed.
No scenario or oracle weakened. Run the full original nine-case boundary.
