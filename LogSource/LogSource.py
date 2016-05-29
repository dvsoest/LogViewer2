# eflag: FileType = Python3

import sys
from urllib import request, error
from Parser import Parser

class LogSource:
    def __init__(self):
        self.logsource = ""
        self.lines = []
        self.sourcetype = None

    def Reload(self):
        self.lines = []
        if self.sourcetype == 'file':
            self.OpenLogFile(self.logsource)
        elif self.sourcetype == 'http':
            self.OpenHttpLog(self.logsource)

    def OpenLogFile(self, fileName):
        try:
            self.logsource = fileName
            input = open(fileName)
            self.lines = input.readlines()
            log = Parser.Parser()
            for line in self.lines:
                log.addLogLine(line)
            input.close()
            self.sourcetype = 'file'
        except IOError as exc:
            self.lastError = 'IOError: ' + str(exc)
        except:
            if self.lastError == '':
                self.lastError = 'Unexpected error: ' + str(sys.exc_info()[1])
                print("Unexpected error:", sys.exc_info()[0])
        return log

    def OpenHttpLog(self, url):
        try:
            filehandle = request.urlopen(url, None, 1)
            file = str(filehandle.read(), "utf-8")
            lines = file.split("\n")
            log = Parser.Parser()
            for line in lines:
                log.addLogLine(line)
            self.logsource = url
            self.sourcetype = 'http'
        except TimeoutError:
            print("Timeout occurred when accessing ", url)
        except error.URLError:
            print("http error when accessing ", url)
        except:
            print("Unexpected error: ", sys.exc_info()[0])
        return log
