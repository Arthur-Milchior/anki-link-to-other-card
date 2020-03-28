from aqt import gui_hooks, mw
from aqt.editor import Editor
from aqt.webview import WebContent

from .consts import addon_package


def loadNote(self):
    self.web.eval(f"""add_link_editor()""")


gui_hooks.editor_did_load_note.append(loadNote)


def on_webview_will_set_content(web_content: WebContent, context):
    if not isinstance(context, Editor):
        return
    web_content.js.append(f"/_addons/{addon_package}/js.js")
    web_content.js.append(f"/_addons/{addon_package}/editor.js")


gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
