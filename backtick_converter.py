import re

from aqt.editor import Editor

CODE_BLOCK_REGEX = re.compile(r'(?<!\\)```')
CODE_TAG_REGEX = re.compile(r'(?<![\\`])`(?!`)')
ESCAPED_BACK_TICK_REGEX = re.compile(r'(?<!\\)\\`')


def replace_triple_back_ticks(html: str) -> str:
    # Convert all triple back ticks to <pre><code>
    tag = "<pre><code>"
    return close_tags(CODE_BLOCK_REGEX.sub(tag, html), tag, "</code></pre>", False)


def replace_single_back_ticks(html: str) -> str:
    # Convert all back ticks to <code>
    tag = "<code>"
    return close_tags(CODE_TAG_REGEX.sub(tag, html), tag, "</code>", False)


def close_tags(html: str, open_tag: str, closed_tag: str, in_code_block: bool) -> str:
    pos = html.find(open_tag)

    if pos == -1:  # find returns -1 if not found
        return html
    endpos = pos + len(open_tag)
    if in_code_block:
        return html[:pos] + closed_tag + close_tags(html[endpos:], open_tag, closed_tag, False)
    return html[:endpos] + close_tags(html[endpos:], open_tag, closed_tag, True)


def cleanup_escaped_back_ticks(html: str) -> str:
    return ESCAPED_BACK_TICK_REGEX.sub("`", html)


def replace_all_backticks(html: str, _: Editor) -> str:
    return cleanup_escaped_back_ticks(
        replace_triple_back_ticks(
            replace_single_back_ticks(html)))
