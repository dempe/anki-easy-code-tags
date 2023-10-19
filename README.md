# Easy Code Blocks/Tags for [Anki](https://apps.ankiweb.net/)

Convert backticks to HTML `<code>` tags in the Anki editor.

This makes the Anki editor parse backticks as Markdown.

Single backticks (\`x == 2\`) will be converted like so `<code>x == 2</code>`.

Triple backticks (\`\`\`x == 2\`\`\`) will be converted like so `<pre><code>x == 2</pre></code>`.

Append a newline-delimited, alphanumeric string to a triple backtick to add a class.

```
   \```php
   echo "hi";
   \```
```

(Note the newline after `php`!) This will be converted to:

```xml
   <pre><code class="language-php">echo "hi";</code></pre>
```

Also works with `<br>` instead of "raw" newline, since the Anki editor automatically inserts `<br>`

```
   \```php<br>
   echo "hi";
   \```
```

Many popular JS-based syntax highlighters ([highlight.js](https://highlightjs.org/), [prismjs](https://prismjs.com/)) can automatically detect what language you're using, but sometimes you have to be explicit and specify the language yourself.

**A few notes**:

- The text in the editor is updated automatically when you...
  1. Jump to a new field
  2. Or save/submit your edits (Ctrl-Enter or click "save")
- The text _displayed_ in the editor is **NOT** updated automatically
  - The new text will be shown next time you view the card in the editor (in the browser, you can hit Ctrl-n, Ctrl-p to go to the next card and back to "refresh" it). 

**Next steps**:

1. Add a hotkey to insert a pair of backticks and a hotkey to insert a pair of triple backticks
2. Add a UI button to insert a pair of backticks and a UI button to insert a pair of triple backticks
3. Make the hotkeys and UI buttons work on selected text
4. Possibly extend functionality to blockquotes (another missing feature in the Anki editor)