import re

from aqt.editor import Editor
from typing import List

# Use a negative lookbehind to find three consecutive backticks not preceded by a backslash
CODE_BLOCK_REGEX = re.compile(r'(?<!\\)```')

# Use a negative lookbehind and negative lookahead to find a single backtick not preceded by a backslash and to preceded or followed by another backtick
CODE_TAG_REGEX = re.compile(r'(?<![\\`])`(?!`)')

# Find backticks preceded by a backslash
ESCAPED_BACK_TICK_REGEX = re.compile(r'(?<!\\)\\`')

# Parse the language for each code block. Languages here: https://highlightjs.org/download
CODE_BLOCK_LANG_REGEX = re.compile(r'<pre><code>([a-z0-9_-]+?)\n')


def find_languages(html: str) -> List[str]:
    """Returns a list of each alphanumeric string that immediately follows <pre><code>"""
    languages = []
    for match in CODE_BLOCK_LANG_REGEX.finditer(html):
        languages.append(match.group(1))
    return languages


def replace_language_with_class(html: str, langauges: List[str]) -> str:
    """Given some HTML and a list of languages, adds an HTML class, "language-*", to each <pre><code>"""
    for language in langauges:
        regex = re.compile('<pre><code>' + language + '\n')
        replacement = f"<pre><code class=\"language-{language}\">"
        html = regex.sub(replacement, html)
    return html


def replace_triple_back_ticks(html: str) -> str:
    """Convert ALL triple backticks to <pre><code>"""
    tag = "<pre><code>"
    return close_tags(CODE_BLOCK_REGEX.sub(tag, html), tag, "</code></pre>", False)


def replace_single_back_ticks(html: str) -> str:
    """Convert ALL backticks to <code>"""
    tag = "<code>"
    return close_tags(CODE_TAG_REGEX.sub(tag, html), tag, "</code>", False)


def close_tags(html: str, open_tag: str, closed_tag: str, in_code_block: bool) -> str:
    """Recursively replaces every other instance of <code> or <pre><code> with </code> or </pre></code> respectively"""
    pos = html.find(open_tag)

    # Find returns -1 if not found
    if pos == -1:
        return html

    endpos = pos + len(open_tag)

    # This is needed for strings with mixed ` and <code>
    # If there already exists a complete codeblock,
    # this prevents the algorithm from closing this already existing code block at the next code block's start.
    closed_tag_pos = html.find(closed_tag)
    if closed_tag_pos != -1 and closed_tag_pos <= pos:
        in_code_block = False

    if in_code_block:
        return html[:pos] + closed_tag + close_tags(html[endpos:], open_tag, closed_tag, False)
    return html[:endpos] + close_tags(html[endpos:], open_tag, closed_tag, True)


def cleanup_escaped_back_ticks(html: str) -> str:
    return ESCAPED_BACK_TICK_REGEX.sub("`", html)


def replace_all_backticks(html: str, _: Editor) -> str:
    html = cleanup_escaped_back_ticks(
        replace_triple_back_ticks(
            replace_single_back_ticks(html)))
    languages = find_languages(html)

    return replace_language_with_class(html, languages)
