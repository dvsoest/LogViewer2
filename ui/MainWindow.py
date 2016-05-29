# eflag: FileType = Python3

"""
Module implementing MainWindow.
"""

from PyQt5.QtWidgets import QMainWindow,  QFileDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt

import re

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
        self.logsource = None
    
    @pyqtSlot()
    def on_btnParse_clicked(self):
        """
        Slot documentation goes here.
        """
        self.logsource.Reload()
        #self.ParseAndShow(self.logsource.logsource, self.logsource, self.txtReToMatch.text())

    def ParseAndShow(self, sourcename, log, filtertext):
        log.parseLog()
        self.lblPath.setText("Parsed " + str(len(log.parsedRecords)) + " lines from " + sourcename)
        self.tvResult.clear()
        self.tvResult.setRowCount(len(log.parsedRecords))
        self.tvResult.setColumnCount(6)
        filterre = re.compile(str(filtertext))

        if log.lastError != '':
            self.lblPath.setText(log.lastError)
        else:
            for logrecord in log.parsedRecords:
                self.insertTableItem(logrecord.index - 1, 0, logrecord.logTime)
                self.insertTableItem(logrecord.index - 1, 1, logrecord.logSeverity)
                self.insertTableItem(logrecord.index - 1, 2, logrecord.logJavaMethod)
                self.insertTableItem(logrecord.index - 1, 3, logrecord.logUser)
                self.insertTableItem(logrecord.index - 1, 4, logrecord.logPage)
                self.insertTableItem(logrecord.index - 1, 5, logrecord.logMessage)
                recordinfilter=(filtertext == '') or (filterre.search(logrecord.logLine))
                if not recordinfilter or not logrecord.successfullyParsed:
                    self.tvResult.setRowHidden(logrecord.index - 1, True)
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
        if fName[0] != '':
            self.logsource = LogSource.LogSource()
            log = self.logsource.OpenLogFile(fName[0])
            self.ParseAndShow(fName[0], log, self.txtReToMatch.text())

    @pyqtSlot()
    def on_actionOpen_http_log_triggered(self):
        dialog = UrlDialog()
        url = dialog.showDialog()
        self.lblPath.setText(url)
        self.logsource = LogSource.LogSource()
        log = self.logsource.OpenHttpLog(url)
        self.ParseAndShow(url,log, self.txtReToMatch.text())

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

    @pyqtSlot()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F5:
            self.logsource.Reload()