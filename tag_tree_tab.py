# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore


class TagTreeTab(QtGui.QWidget):

    def __init__(self):
        super(TagTreeTab, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.model = QtGui.QSortFilterProxyModel()

        self.tree_view = QtGui.QTreeView()
        self.tree_view.setRootIsDecorated(False)
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_item_model = QtGui.QStandardItemModel(0, 2)
        self.tree_item_model.setHeaderData(0, QtCore.Qt.Horizontal, "Tag")
        self.tree_item_model.setHeaderData(1, QtCore.Qt.Horizontal, "Text")

        self.tree_item_model.setItem(0, 0, QtGui.QStandardItem(""))
        self.tree_item_model.setItem(0, 1, QtGui.QStandardItem(""))
        self.model.setSourceModel(self.tree_item_model)

        self.main_vbox = QtGui.QVBoxLayout()
        self.main_vbox.addWidget(self.tree_view)
        self.setLayout(self.main_vbox)

    def set_tree_item(self, html_list):
        for index in range(0, len(html_list)):
            url_item = QtGui.QStandardItem(str(html_list[index][0]))
            title_item = QtGui.QStandardItem(str(html_list[index][1]))

            self.tree_item_model.setItem(index, 0, url_item)
            self.tree_item_model.setItem(index, 1, title_item)

