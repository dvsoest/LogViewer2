# eflag: FileType = Python3

import re
import sys

standardBlueriqRe = "(\d{4}-\d{2}-\d{2}) ([\d:]{8}).(\d{3}) (\S*)\s*([a-zA-Z.]*)\sruntimeSessionId=\"(\S*)\" \
userId=\"(\S*)\" projectName=\"(\S*)\" projectVersion=\"(\S*)\" currentPageName=\"(\S*)\" - (.*)"
backupBlueriqRe = "Caused by:\s([^:]*):\s(.*)"
standardReObj = re.compile(str(standardBlueriqRe))
backupReObj = re.compile(str(backupBlueriqRe))


class Parser:

    def parseLog(self, lines):
        self.cleanStuff()
        try:
            linecount = 0
            for line in lines:
                linecount += 1
                match = standardReObj.match(line)
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
                    logEntry = BlueriqLogEntry(linecount, True, logDate, logTime, logMilliseconds, logSeverity,
                                               logJavaMethod, logSessionId, logUser, logProject, logBranch, logPage,
                                               logMessage, line)
                else:
                    match = backupReObj.match(line)
                    if match:
                        logJavaMethod = match.groups()[0]
                        logMessage = match.groups()[1]
                        logEntry = BlueriqLogEntry(linecount, True, logSeverity ="Caused by",
                                                   logJavaMethod=logJavaMethod, logMessage=logMessage, logLine=line)
                    else:
                        logEntry = BlueriqLogEntry(linecount, False, logLine=line)

                self.parsedRecords.append(logEntry)
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


class BlueriqLogEntry:
    def __init__(self, index, successfullyParsed, logDate=None, logTime=None, logMilliseconds=None, logSeverity=None,
                 logJavaMethod=None, logSessionId=None, logUser=None, logProject=None, logBranch=None, logPage=None,
                 logMessage=None, logLine=None):
        self.index = index
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
        self.logLine = logLine
