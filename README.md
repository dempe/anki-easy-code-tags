# Easy Code Blocks/Tags for [Anki](https://apps.ankiweb.net/)

Convert backticks to HTML `<code>` tags in the Anki editor.

This makes the Anki editor parse backticks as Markdown.

- **Single backticks**: (`` `x == 2` ``) will be converted like so `<code>x == 2</code>`.
- **Triple backticks**: (`` ```x == 2``` ``) will be converted like so `<pre><code>x == 2</pre></code>`.

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

FWIW, to install a syntax highlighter: 

1. Copy the downloaded JS code into your `collection.media` directory (for example, `highlight.min.js`)
2. Prefix the JS library name with `_` (for example, `highlight.min.js` -> `_highlight.min.js`)
   1. This is so Anki doesn't try to delete it since it's not being referenced by any field
3. Copy an associated CSS file for styling and also prefix it with an `_` (e.g., `_github-dark.min.css`)
4. Edit your cards to call the JS library and load the CSS like so:

```xml
<link rel="stylesheet" href="_github-dark.min.css">
<script src="_highlight.min.js"></script>
<script>hljs.highlightAll();</script>
```

## A few notes

- The text in the editor is updated automatically when you...
  1. Jump to a new field
  2. Or save/submit your edits (Ctrl-Enter or click "save")
- The text _displayed_ in the editor is **NOT** updated automatically
  - The new text will be shown next time you view the card in the editor (in the browser, you can hit Ctrl-n, Ctrl-p to go to the next card and back to "refresh" it). 

## Next steps

1. Add a hotkey to insert a pair of backticks and a hotkey to insert a pair of triple backticks
2. Add a UI button to insert a pair of backticks and a UI button to insert a pair of triple backticks
3. Make the hotkeys and UI buttons work on selected text
