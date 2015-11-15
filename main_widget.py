# -*- coding: utf-8 -*-

import sys
import webbrowser
import lxml.html
from PyQt4 import QtGui, QtCore

import tag_tree_tab
import error_message_box
import network


class MainWidget(QtGui.QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.init_ui()
        self.tag_list = []

    def init_ui(self):
        url_label = QtGui.QLabel("対象URL")

        self.url_line_edit = QtGui.QLineEdit(self)
        self.url_line_edit.setText("")

        self.analysis_button = QtGui.QPushButton("解析", self)
        self.analysis_button.clicked.connect(self.analysis_btn_action)

        load_button = QtGui.QPushButton("概定のブラウザで開く", self)
        load_button.clicked.connect(self.open_browser)

        self.url_hbox = QtGui.QHBoxLayout()

        self.url_hbox.addWidget(url_label)
        self.url_hbox.addWidget(self.url_line_edit)
        self.url_hbox.addWidget(self.analysis_button)
        self.url_hbox.addWidget(load_button)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.addLayout(self.url_hbox)

        self.tag_tree_tab = tag_tree_tab.TagTreeTab()

        tab_widget = QtGui.QTabWidget()
        tab_widget.addTab(self.tag_tree_tab, "タグ")
        self.main_vbox.addWidget(tab_widget)

        self.setLayout(self.main_vbox)

    def analysis_btn_action(self):
        if self.is_inputed_url_edit_text():
            url = network.reauest_html(self.url_line_edit.text())
            self.analysis(url)

    def is_inputed_url_edit_text(self):
        if self.url_line_edit.text() == "":
            msg_box = error_message_box.ErrorMessageBox("URLを入力してください")
            msg_box.exec_()
            return False

        return True

    def analysis(self, target_html):
        root = lxml.html.fromstring(target_html)
        self.traverse(root)
        self.tag_tree_tab.set_tree_item(self.tag_list)

    def traverse(self, root, depth = 0):
        tag = [str(root.tag), str(root.text)]
        self.tag_list.append(tag)

        for child in root:
            self.traverse(child, depth + 1)

    def open_browser(self):
        if not self.url_line_edit.text():
            msg_box = error_message_box.ErrorMessageBox("URLを入力してください")
            msg_box.exec_()
            return
        webbrowser.open(self.url_line_edit.text())

