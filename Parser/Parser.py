# eflag: FileType = Python3

import re
import sys

standardBlueriqRe = "(\d{4}-\d{2}-\d{2}) ([\d:]{8}).(\d{3}) (\S*)\s*([a-zA-Z.]*)\sruntimeSessionId=\"(\S*)\" \
userId=\"(\S*)\" projectName=\"(\S*)\" projectVersion=\"(\S*)\" currentPageName=\"(\S*)\" - (.*)"
backupBlueriqRe = "Caused by:\s([^:]*):\s(.*)"
standardReObj = re.compile(str(standardBlueriqRe))
backupReObj = re.compile(str(backupBlueriqRe))

class Parser:

    def __init__(self):
        self.parsedRecords = []
        self.lastError = ''

    def addLogLine(self, text):
        newentry = LogEntry( len(self.parsedRecords) + 1, logLine=text)
        self.parsedRecords.append(newentry)

    def parseLog(self):
        try:
            for logentry in self.parsedRecords:
                match = standardReObj.match(logentry.logLine)
                if match:
                    logDate = match.groups()[0]
                    logTime = match.groups()[1]
                    logMilliseconds = match.groups()[2]
                    logSeverity = match.groups()[3]
                    logJavaMethod = match.groups()[4]
                    logSessionId = match.groups()[5]
                    logUser = match.groups()[6]
                    logProject = match.groups()[7]
                    logBranch = match.groups()[8]
                    logPage = match.groups()[9]
                    logMessage = match.groups()[10]
                    logentry.Update(True, logDate, logTime, logMilliseconds, logSeverity,
                                        logJavaMethod, logSessionId, logUser, logProject, logBranch, logPage,
                                        logMessage)
                else:
                    match = backupReObj.match(logentry.logLine)
                    if match:
                        logJavaMethod = match.groups()[0]
                        logMessage = match.groups()[1]
                        logentry.Update(successfullyParsed=True, logSeverity ="Caused by",
                                        logJavaMethod=logJavaMethod, logMessage=logMessage)
                    else:
                        logentry.Update(successfullyParsed=False)
        except IndexError as exc:
            self.lastError = 'IndexError: ' + str(exc)
        except:
            if self.lastError == '':
                self.lastError = 'Unexpected error: ' + str(sys.exc_info()[1])
                print("Unexpected error:", sys.exc_info()[0])
            pass

    def cleanStuff(self):
        self.parsedRecords = []
        self.lastError = ''


class LogEntry:
    def __init__(self, index, logLine ):
        self.index = index
        self.logLine = logLine

    def Update(self, successfullyParsed = False, logDate=None, logTime=None, logMilliseconds=None, logSeverity=None,
                 logJavaMethod=None, logSessionId=None, logUser=None, logProject=None, logBranch=None, logPage=None,
                 logMessage=None):
        self.successfullyParsed = successfullyParsed
        self.logDate = logDate
        self.logTime = logTime
        self.logMilliseconds = logMilliseconds
        self.logSeverity = logSeverity
        self.logJavaMethod = logJavaMethod
        self.logSessionId = logSessionId
        self.logUser = logUser
        self.logProject = logProject
        self.logBranch = logBranch
        self.logPage = logPage
        self.logMessage = logMessage
