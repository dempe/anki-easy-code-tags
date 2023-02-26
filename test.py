import unittest

from backtick_converter import replace_single_back_ticks, replace_triple_back_ticks, cleanup_escaped_back_ticks, \
    replace_all_backticks


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
        self.assertEqual("<pre><code>x == 2</code></pre> oops! <pre><code>",
                         replace_triple_back_ticks("```x == 2``` oops! ```"))

    def test_cleanup_escaped_back_ticks(self):
        self.assertEqual('`', cleanup_escaped_back_ticks(r'\`'))
        self.assertEqual(r'\\`', cleanup_escaped_back_ticks(r'\\`'))

    def test_all_together(self):
        self.assertEqual(r'<code>x == 2</code> <pre><code>this is a code block</code></pre>',
                         replace_all_backticks(r'`x == 2` ```this is a code block```', None))
        self.assertEqual(r'<code>x == 2</code> ```this is a code block<pre><code>',
                         replace_all_backticks(r'`x == 2` \```this is a code block```', None))

    def test_misc(self):
        self.assertEqual(r'<pre><code>code block</code></pre> with <code>code</code>',
                         replace_all_backticks(r'```code block``` with `code`', None))

