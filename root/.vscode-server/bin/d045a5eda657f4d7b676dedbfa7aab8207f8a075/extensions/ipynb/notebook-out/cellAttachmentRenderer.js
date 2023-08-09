// extensions/ipynb/notebook-src/cellAttachmentRenderer.ts
async function activate(ctx) {
  const markdownItRenderer = await ctx.getRenderer("vscode.markdown-it-renderer");
  if (!markdownItRenderer) {
    throw new Error(`Could not load 'vscode.markdown-it-renderer'`);
  }
  markdownItRenderer.extendMarkdownIt((md) => {
    const original = md.renderer.rules.image;
    md.renderer.rules.image = (tokens, idx, options, env, self) => {
      const token = tokens[idx];
      const src = token.attrGet("src");
      const attachments = env.outputItem.metadata.attachments;
      if (attachments && src) {
        const imageAttachment = attachments[src.replace("attachment:", "")];
        if (imageAttachment) {
          const objEntries = Object.entries(imageAttachment);
          if (objEntries.length) {
            const [attachmentKey, attachmentVal] = objEntries[0];
            const b64Markdown = "data:" + attachmentKey + ";base64," + attachmentVal;
            token.attrSet("src", b64Markdown);
          }
        }
      }
      if (original) {
        return original(tokens, idx, options, env, self);
      } else {
        return self.renderToken(tokens, idx, options);
      }
    };
  });
}
export {
  activate
};
