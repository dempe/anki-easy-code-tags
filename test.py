import unittest

from backtick_converter import *


class BackTickUnitTests(unittest.TestCase):
    def test_replaces_single_back_ticks(self):
        self.assertEqual("<code>x == 2</code>", replace_single_back_ticks("`x == 2`"))

    def test_does_not_replace_escaped_single_back_ticks(self):
        self.assertEqual(r'\`x == 2', replace_single_back_ticks(r'\`x == 2'))

    def test_single_replace_does_not_replace_triple_back_ticks(self):
        self.assertEqual("```x == 2", replace_single_back_ticks("```x == 2"))
        self.assertEqual("```x == 2```", replace_single_back_ticks("```x == 2```"))

    def test_handles_extraneous_single_back_ticks(self):
        """Applying Occam's Razor here.
            If the user wants a literal back tick, they need to escape it."""
        self.assertEqual("<code>x == 2``", replace_single_back_ticks("`x == 2``"))
        self.assertEqual(r'<code>x == 2</code>\`', replace_single_back_ticks(r'`x == 2`\`'))  # Must escape

    def test_replaces_triple_back_ticks(self):
        self.assertEqual("<pre><code>x == 2</code></pre>", replace_triple_back_ticks("```x == 2```"))

    def test_does_not_replace_escaped_triple_back_ticks(self):
        self.assertEqual(r'\```x == 2', replace_triple_back_ticks(r'\```x == 2'))

    def test_handles_extraneous_triple_back_ticks(self):
        """Applying Occam's Razor here.
            If the user wants a literal back tick, they need to escape it."""
        expected = '<pre><code>x == 2</code></pre> oops! <pre><code>'
        actual = replace_triple_back_ticks('```x == 2``` oops! ```')

        self.assertEqual(expected, actual)

    def test_cleanup_escaped_back_ticks(self):
        self.assertEqual('`', cleanup_escaped_back_ticks(r'\`'))
        self.assertEqual(r'\\`', cleanup_escaped_back_ticks(r'\\`'))

    def test_all_together(self):
        expected = r'<code>x == 2</code> <pre><code>this is a code block</code></pre>'
        actual = replace_all_backticks(r'`x == 2` ```this is a code block```', None)
        self.assertEqual(expected, actual)

        expected = r'<code>x == 2</code> ```this is a code block<pre><code>'
        actual = replace_all_backticks(r'`x == 2` \```this is a code block```', None)
        self.assertEqual(expected, actual)

    def test_misc(self):
        expected = r'<pre><code>code block</code></pre> with <code>code</code>'
        actual = replace_all_backticks(r'```code block``` with `code`', None)

        self.assertEqual(expected, actual)

    def test_mixed_back_ticks_and_code_tags(self):
        expected = '<code>x == 2</code> mixed with <code>x == 4</code> backticks'
        actual = replace_all_backticks('<code>x == 2</code> mixed with `x == 4` backticks', None)

        self.assertEqual(expected, actual)

    def test_find_languages_newline_delimited(self):
        html = '<pre><code>python\ndef add()\n</pre></code><pre><code>php\necho "hi"</pre></code>'
        expected = ['python', 'php']
        self.assertEqual(expected, find_languages(html))

    def test_find_languages_br_delimited(self):
        html = '<pre><code>python<br>def add()\n</pre></code><pre><code>php<br>echo "hi"</pre></code>'
        expected = ['python', 'php']
        self.assertEqual(expected, find_languages(html))

    def test_replace_language_with_class(self):
        html = '<pre><code>python\ndef add()\n</pre></code><pre><code>php\necho "hi"</pre></code>'
        languages = ['python', 'php']
        expected = '<pre><code class="language-python">def add()\n</pre></code><pre><code class="language-php">echo "hi"</pre></code>'
        actual = replace_language_with_class(html, languages)

        self.assertEqual(expected, actual)
