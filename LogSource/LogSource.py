# eflag: FileType = Python3

import sys
from urllib import request, error

url = "http://hector:9000"

class LogSource:
    def __init__(self):
        self.logsource = ""
        self.lines = []

    def OpenLogFile(self, fileName):
        self.CleanStuff()
        try:
            self.logsource = fileName
            input = open(fileName)
            self.lines = input.readlines()
            input.close()
        except IOError as exc:
            self.lastError = 'IOError: ' + str(exc)
        except:
            if self.lastError == '':
                self.lastError = 'Unexpected error: ' + str(sys.exc_info()[1])
                print("Unexpected error:", sys.exc_info()[0])
        pass

    def OpenHttpLog(self, url):
        self.CleanStuff()
        try:
            filehandle = request.urlopen(url, None, 1)
            self.lines = filehandle.read()
        except TimeoutError:
            print("Timeout occurred when accessing ", url)
        except error.URLError:
            print("http error when accessing ", url)
        except:
            print("Unexpected error: ", sys.exc_info()[0])

    def CleanStuff(self):
        self.logsource = ""
        self.lines = []