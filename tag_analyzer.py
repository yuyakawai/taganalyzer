# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import main_window

def main():
    app = QtGui.QApplication(sys.argv)
    window = main_window.MainWindow()
    app.exec_()

# Entry point
if __name__ == "__main__":
    main()

