from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer
from aqt.webview import WebContent

from .consts import addon_package


def on_webview_will_set_content(web_content: WebContent, context):
    if not isinstance(context, Reviewer):
        return
    web_content.js.append(f"/_addons/{addon_package}/js.js")
    web_content.js.append(f"/_addons/{addon_package}/reviewer.js")


gui_hooks.webview_will_set_content.append(on_webview_will_set_content)


def show(c):
    mw.web.eval(f"""add_link_reviewer()""")


gui_hooks.reviewer_did_show_answer.append(show)
gui_hooks.reviewer_did_show_question.append(show)
