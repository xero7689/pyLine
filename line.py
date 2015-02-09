#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

from PyQt4 import QtCore, QtGui


class Line(QtGui.QStackedWidget):
    def __init__(self, parent=None):
        super(Line, self).__init__(parent)


class Login(QtGui.QWidget):
    """ Login Widget
    You can try using QStackWidget...to implement switch widget.
    """
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Login
        pass


class Main(QtGui.QWidget):
    """LINE Main Process
    """
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)


def main():
    pass

if __name__ == "__main__":
    main()