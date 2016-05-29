# eflag: FileType = Python3

"""
Module implementing MainWindow.
"""

from PyQt5.QtWidgets import QMainWindow,  QFileDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot


from Parser import Parser

from LogSource import LogSource

from ui.LogParserTable import Ui_MainWindow
from ui.OpenUrlDialog import UrlDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btnParse_clicked(self):
        """
        Slot documentation goes here.
        """
        self.ParseAndShow()

    def ParseAndShow(self, fName):
        self.tvResult.clear()
        #fName = self.lblPath.text()
        logsource = LogSource.LogSource()
        logsource.OpenLogFile(fName)
        parser = Parser.Parser()
        parser.parseLog(logsource.lines)
        self.lblPath.setText("Parsed " + str(len(parser.parsedRecords)) + " lines from " + fName)
        self.tvResult.setRowCount(len(parser.parsedRecords))
        self.tvResult.setColumnCount(6)

        if parser.lastError != '':
            self.lblPath.setText(parser.lastError)
        else:
            for logRecord in parser.parsedRecords:
                self.insertTableItem(logRecord.index - 1, 0, logRecord.logTime)
                self.insertTableItem(logRecord.index - 1, 1, logRecord.logSeverity)
                self.insertTableItem(logRecord.index - 1, 2, logRecord.logJavaMethod)
                self.insertTableItem(logRecord.index - 1, 3, logRecord.logUser)
                self.insertTableItem(logRecord.index - 1, 4, logRecord.logPage)
                self.insertTableItem(logRecord.index - 1, 5, logRecord.logMessage)
                if not logRecord.successfullyParsed:
                    self.tvResult.setRowHidden(logRecord.index - 1, True)
        self.tvResult.resizeColumnsToContents()

    def insertTableItem(self, row, column, text):
        cellitem = QTableWidgetItem()
        cellitem.setText(text)
        cellitem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tvResult.setItem(row, column, cellitem)

    @pyqtSlot()
    def on_actionOpen_Log_File_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog()
        fName = dialog.getOpenFileName(self,"Select a Blueriq log file to parse", "", "*.log")
        # self.lblPath.setText(fName[0])
        self.ParseAndShow(fName[0])

    @pyqtSlot()
    def on_actionOpen_http_log_triggered(self):
        dialog = UrlDialog()
        url = dialog.showDialog()
        self.lblPath.setText(url)

    @pyqtSlot()
    def on_action_Quit_triggered(self):
        """
        Slot documentation goes here.
        """
        quit()
    
    @pyqtSlot()
    def on_action_About_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
