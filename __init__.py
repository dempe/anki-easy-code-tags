from aqt import gui_hooks
from .backtick_converter import replace_all_backticks

gui_hooks.editor_will_munge_html.append(replace_all_backticks)
