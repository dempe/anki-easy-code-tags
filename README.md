# Easy Code Tags for [Anki](https://apps.ankiweb.net/)

Convert backticks to HTML `<code>` tags in the Anki editor.

This makes the Anki editor parse backticks as Markdown.

Single backticks (\`x == 2\`) will be converted like so `<code>x == 2</code>`.

Triple backticks (\`\`\`x == 2\`\`\`) will be coverted like so `<pre><code>x == 2</pre></code>`.

**A few notes**:

- The text in the editor is updated automatically when you...
  1. Jump to a new field
  2. Or save/submit your edits (Ctrl-Enter or click "save")
- The text _displayed_ in the editor is **NOT** udpated automatically
  - The new text will be shown next time you view the card in the editor (you can hit Ctrl-n, Ctrl-p to go to the next card and back to "refresh" it). 
