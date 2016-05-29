# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Eric Workspace\LogParser\ui\LogParser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPath = QtWidgets.QLabel(self.centralWidget)
        self.lblPath.setObjectName("lblPath")
        self.verticalLayout.addWidget(self.lblPath)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtReToMatch = QtWidgets.QLineEdit(self.centralWidget)
        self.txtReToMatch.setObjectName("txtReToMatch")
        self.horizontalLayout.addWidget(self.txtReToMatch)
        self.btnParse = QtWidgets.QPushButton(self.centralWidget)
        self.btnParse.setObjectName("btnParse")
        self.horizontalLayout.addWidget(self.btnParse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tvResult = QtWidgets.QTreeWidget(self.centralWidget)
        self.tvResult.setObjectName("tvResult")
        self.verticalLayout.addWidget(self.tvResult)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 744, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_Log_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log_File.setObjectName("actionOpen_Log_File")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.menu_File.addAction(self.actionOpen_Log_File)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.actionTest)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log Parser"))
        self.lblPath.setText(_translate("MainWindow", "Please, load a log file"))
        self.btnParse.setText(_translate("MainWindow", "Parse Log File"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionOpen_Log_File.setText(_translate("MainWindow", "Open &Log File"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.actionTest.setText(_translate("MainWindow", "Test2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

