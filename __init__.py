from aqt import gui_hooks
from aqt.editor import Editor


def replace_backticks(html: str, _: Editor) -> str:
    """Loop through each char in html, check for backtick, convert to <code> or </code> accordingly."""

    in_code_block = False
    new_html = ""
    for char in html:
        if char == '`' and not in_code_block:
            in_code_block = True
            new_html = new_html + "<code>"
            continue
        if char == '`' and in_code_block:
            in_code_block = False
            new_html = new_html + "</code>"
            continue
        new_html = new_html + char

    return new_html


gui_hooks.editor_will_munge_html.append(replace_backticks)
