from aqt import dialogs, gui_hooks, mw

from . import editor, reviewer

mw.addonManager.setWebExports(__name__, r".*(css|js)")


def onBridge(handled, cmd, reviewer):
    prefix = "browser search:"
    if not cmd.startswith(prefix):
        return handled
    search = cmd[len(prefix):]
    browser = dialogs.open("Browser", reviewer.mw)
    browser.model.search(search)
    return (True, None)


gui_hooks.webview_did_receive_js_message.append(onBridge)
