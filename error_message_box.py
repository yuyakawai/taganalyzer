# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class ErrorMessageBox(QtGui.QMessageBox):

    def __init__(self, text):
        super(ErrorMessageBox, self).__init__()

        self.setWindowTitle("ERROR")
        self.setText(text)
        self.setIcon(3)

