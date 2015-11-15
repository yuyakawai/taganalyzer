# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

import main_widget

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.help_menu = self.menuBar().addMenu("ヘルプ(&H)")
        about_action = QtGui.QAction("Web Scraper について",
                                     self,
                                     triggered = self.show_about_dialog)

        self.help_menu.addAction(about_action)

        self.widget = main_widget.MainWidget()
        self.setCentralWidget(self.widget) 

        self.setWindowTitle("web スクレイピング")
        self.resize(900, 600)
        self.show()

    def show_about_dialog(self):
        QtGui.QMessageBox.about(self,
                                "Tag Analyzer について",
                                "<b>Tag Analyzer について</b>"
                                "<br>version : 1.0"
                                "<br>Copyright © 2015 Yuya Kawai. All Rights Reserved.")

