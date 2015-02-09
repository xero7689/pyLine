#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

from PyQt4 import QtGui, QtCore
# for debug
import sys


class Login(QtGui.QWidget):
    """ Login Widget
    You can try using QStackWidget...to implement switch widget.
    """
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Layout
        hl = QtGui.QVBoxLayout()
        layout_list = []
        layout_id = QtGui.QHBoxLayout()
        layout_pwd = QtGui.QHBoxLayout()
        layout_list.append(layout_id)
        layout_list.append(layout_pwd)

        # Logo
        logo = QtGui.QPixmap("image/line.png")
        logo = logo.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        lb = QtGui.QLabel(self)  # QLabel provides text or image display.
        lb.setPixmap(logo)

        # Input

        lb_id = QtGui.QLabel("ID: ")
        lb_pwd = QtGui.QLabel("PW: ")
        edit_id = QtGui.QLineEdit()
        edit_pwd = QtGui.QLineEdit()

        layout_id.addWidget(lb_id)
        layout_id.addStretch()
        layout_id.addWidget(edit_id)
        layout_pwd.addWidget(lb_pwd)
        layout_pwd.addStretch()
        layout_pwd.addWidget(edit_pwd)

        # Init
        hl.addWidget(lb)
        for layout in layout_list:
            hl.addLayout(layout)
        self.setLayout(hl)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()