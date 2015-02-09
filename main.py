#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

import sys

from PyQt4 import QtCore, QtGui


class Line(QtGui.QStackedWidget):
    def __init__(self, parent=None):
        super(Line, self).__init__(parent)


class Main(QtGui.QWidget):
    """LINE Main Process
    """
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)


def main():
    app = QtGui.QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()