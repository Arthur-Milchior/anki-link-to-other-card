# Code originally from https://github.com/ijgnd/anki21__editor_add_hyperlink/blob/master/src/window.py

import json

from aqt.qt import (QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton,
                    QVBoxLayout)

from .helper_functions import escape_html_chars

# size of the dialog windows
DIALOG_SIZE_X = 350
DIALOG_SIZE_Y = 200
MIN_COMBOBOX_WIDTH = 140


class Hyperlink:
    def __init__(self, other, parent_window, selected_text, to_create="a hyperlink", label="Link to", place_holder="URL", prefix="browser search:", selected_is_url=False):
        self.editor_instance = other
        self.parent_window = parent_window
        self.selected_text = selected_text
        self.selected_is_url = selected_is_url
        self.to_create = to_create
        self.label = label
        self.place_holder = place_holder
        self.prefix = prefix
        self.hyperlink_dialog()

    def hyperlink_dialog(self):
        dialog = QDialog(self.parent_window)
        dialog.setWindowTitle(f"Create {self.to_create}")
        dialog.resize(DIALOG_SIZE_X, DIALOG_SIZE_Y)

        ok_button_anchor = QPushButton("&OK", dialog)
        ok_button_anchor.setEnabled(False)
        ok_button_anchor.clicked.connect(lambda: self.insert_anchor(
            url_edit.text(), urltext_edit.text()))
        ok_button_anchor.clicked.connect(dialog.hide)

        ok_button_anchor.setAutoDefault(True)

        cancel_button_anchor = QPushButton("&Cancel", dialog)
        cancel_button_anchor.clicked.connect(dialog.hide)
        cancel_button_anchor.setAutoDefault(True)

        url_label = QLabel(f"{self.label}:")
        url_edit = QLineEdit()
        url_edit.setPlaceholderText(self.place_holder)
        url_edit.textChanged.connect(lambda: self.enable_ok_button(
            ok_button_anchor, url_edit.text(), urltext_edit.text()))

        urltext_label = QLabel("Text to display:")
        urltext_edit = QLineEdit()
        urltext_edit.setPlaceholderText("Text")
        urltext_edit.textChanged.connect(lambda: self.enable_ok_button(
            ok_button_anchor, url_edit.text(), urltext_edit.text()))

        button_box = QHBoxLayout()
        button_box.addStretch(1)
        button_box.addWidget(cancel_button_anchor)
        button_box.addWidget(ok_button_anchor)

        dialog_vbox = QVBoxLayout()
        dialog_vbox.addWidget(url_label)
        dialog_vbox.addWidget(url_edit)
        dialog_vbox.addWidget(urltext_label)
        dialog_vbox.addWidget(urltext_edit)
        dialog_vbox.addLayout(button_box)
        dialog.setLayout(dialog_vbox)
        # if user already selected text, put it in urltext_edit
        if self.selected_text:
            if self.selected_is_url:
                url_edit.setText(self.selected_text)
                urltext_edit.setFocus()
            else:
                urltext_edit.setText(self.selected_text)
                url_edit.setFocus()
        dialog.exec()

    @staticmethod
    def enable_ok_button(button, url, text):
        if url and text:
            button.setEnabled(True)
        else:
            button.setEnabled(False)

    def create_anchor(self, url, text):
        """
        Create a hyperlink string, where `url` is the hyperlink reference
        and `text` the content of the tag.
        """
        text = escape_html_chars(text)
        return f"<a onclick=\"pycmd('{self.prefix}{url}')\">{text}</a>"

    def insert_anchor(self, url, text):
        """
        Inserts a HTML anchor `<a>` into the text field.
        """
        self.replacement = self.create_anchor(url, text)
