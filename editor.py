import json
import os

from anki.hooks import addHook
from aqt import gui_hooks
from aqt.editor import Editor
from aqt.qt import QKeySequence
from aqt.webview import WebContent

from .config import getUserOption
from .consts import addon_package
from .window import Hyperlink


def loadNote(self):
    self.web.eval(f"""add_link_editor()""")


def keystr(k):
    key = QKeySequence(k)
    return key.toString(QKeySequence.NativeText)


gui_hooks.editor_did_load_note.append(loadNote)
addon_path = os.path.dirname(__file__)


def on_webview_will_set_content(web_content: WebContent, context):
    if not isinstance(context, Editor):
        return
    web_content.js.append(f"/_addons/{addon_package}/js.js")
    web_content.js.append(f"/_addons/{addon_package}/editor.js")


gui_hooks.webview_will_set_content.append(on_webview_will_set_content)


def toggle_browser(editor):
    selected = editor.web.selectedText()
    h = Hyperlink(editor, editor.parentWindow, selected, to_create="Link as Browser search",
                  label="Browser search", prefix="browser search:", place_holder="Search")
    if hasattr(h, "replacement"):
        editor.web.eval(
            "document.execCommand('insertHTML', false, %s);"
            % json.dumps(h.replacement))


Editor.toggle_hyperlink = toggle_browser


def toggle_nid(editor):
    selected = editor.web.selectedText()
    h = Hyperlink(editor, editor.parentWindow, selected, to_create="Link to a node",
                  label="Note", prefix="browser search:nid:", place_holder="Note ID")
    if hasattr(h, "replacement"):
        editor.web.eval(
            "document.execCommand('insertHTML', false, %s);"
            % json.dumps(h.replacement))


Editor.toggle_nid = toggle_nid


def setupEditorButtonsFilter(buttons, editor):
    # note
    if getUserOption("show button for note link", True):
        shortcut_nid = getUserOption("shortcut Note ID", "Ctrl+Shift+N")
        buttons.append(
            editor.addButton(
                os.path.join(addon_path, "icons", "note.svg"),
                "note_button",
                toggle_nid,
                tip="Link to note ({})".format(
                    keystr(shortcut_nid)),
                keys=shortcut_nid
            )
        )

    # browser
    if getUserOption("show button for browser link", True):
        shortcut_browser = getUserOption("shortcut Browser", "Ctrl+Shift+B")
        buttons.append(
            editor.addButton(
                os.path.join(addon_path, "icons", "browser.svg"),
                "browser_button",
                toggle_browser,
                tip="Link to browser search ({})".format(
                    keystr(shortcut_browser)),
                keys=shortcut_browser
            )
        )

    return buttons


addHook("setupEditorButtons", setupEditorButtonsFilter)
