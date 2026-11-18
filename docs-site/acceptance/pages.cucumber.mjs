export default {
  paths: ['acceptance/features/pages.feature'],
  import: ['acceptance/steps/pages.mjs'],
  format: ['progress', 'message:' + process.env.PAGES_EVIDENCE + '/messages.ndjson'],
  parallel: 0,
};
