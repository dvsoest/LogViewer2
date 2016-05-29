#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we receive data from
a QInputDialog dialog.

author: Dick van Soest
last edited: May 2016
"""

import sys
from PyQt5.QtWidgets import (QWidget, QInputDialog, QApplication)


class UrlDialog(QWidget):
    def __init__(self):
        super().__init__()

    def showDialog(self):
        returntext, ok = QInputDialog.getText(self, 'Open log from URL',
                                        'Enter URL of log file:')

        if ok:
            return returntext


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UrlDialog()
    text = ex.showDialog()
    sys.exit(app.exec_())