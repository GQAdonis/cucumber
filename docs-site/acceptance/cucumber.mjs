export default {
  paths: ['acceptance/features/documentation.feature'],
  import: ['acceptance/steps/documentation.mjs'],
  format: ['progress', 'message:' + process.env.DOCS_EVIDENCE + '/messages.ndjson'],
  parallel: 0,
};
