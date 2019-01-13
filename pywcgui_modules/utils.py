from PySide2 import QtCore, QtGui, QtWidgets

# Approprriate headers to avoid any 403 forbidden errors
HDR = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
       "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
       "Accept-Encoding": "none",
       "Accept-Language": "en-US,en;q=0.8",
       "Connection": "keep-alive"}

# Strips non alpha numeric char
def stripNonAlphaNum(text):
    """ Delete non alphanumerical character into a string text and return a list """

    import re
    return re.compile(r"\W+", re.UNICODE).split(text)

def numberOfChar(stringList):
    """ Returns number of char into a list of strings and return a int """

    return sum(len(s) for s in stringList)

def urlReadable(urlsite):
    """ Check if a site url can be analysed or not and return a boolean """

    import urllib2, re

    # Perform a HTTP request by passing URL and setting headers
    req = urllib2.Request(urlsite, headers=HDR)
    try:
        page = urllib2.urlopen(req)
        return True
    except:
        return False

def fileReadable(filepath):
    """ Check if a file path can be analysed or not and return a boolean """

    import os
    if not os.path.isfile(filepath):
        return False
    return True

# Returns file content
def readfile(filepath):
    """ Read a text file and return the content as string """

    with open(filepath) as fp:
        return fp.read()

# Returns url text content
def readurl(urlsite):
    """ Read a site url and return the content as string """

    import urllib2, re

    tagHtml = re.compile(r"<[^>]+>")
    page = None

    # Perform a HTTP request by passing URL and setting headers
    req = urllib2.Request(urlsite, headers=HDR)
    page = urllib2.urlopen(req)

    # Read the response
    content = page.read()

    # Delete uneeded content
    contentNoScript = re.sub(r"(\<script)\s*[^\>]*\>([^\<]*\<\/script>)", "", content)
    contentNoScriptAndStyles = re.sub("r(\<style)\s*[^\>]*\>([^\<]*\<\/style>)", "", contentNoScript)
    contentNoTags = tagHtml.sub("", contentNoScriptAndStyles)
    contentUnescaped = re.sub(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));", " ", contentNoTags)

    return contentUnescaped

def writeDataIntoCsvFile(filePath, filteredStatDict):
    """
        Write data into a csv file
        args :
            - filePath (str): outputfile's full path
            - filteredStatDict (dict): data to write into the output csv file
    """

    import csv

    totalOccur = sum(occur for word, occur in filteredStatDict["wordcount"])

    with open(filePath, "w") as outputcsvfile:
        fieldnames = ["WORD", "TIMES", "SCORE%"]
        writer = csv.DictWriter(outputcsvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, occur in filteredStatDict["wordcount"]:
            writer.writerow({"WORD": word, "TIMES": occur, "SCORE%": float(occur * 100)/totalOccur})

        statWriter = csv.writer(outputcsvfile, delimiter=',')
        statWriter.writerow(['', '', ''])
        statWriter.writerow(['Number of lines', filteredStatDict["nbLines"]])
        statWriter.writerow(['Number of words', filteredStatDict["nbWords"]])
        statWriter.writerow(['Number of characters', filteredStatDict["nbChars"]])


class TableModel(QtCore.QAbstractTableModel):
    """ Model used to populate table into view """

    def __init__(self, datain, headerdata, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headerdata[col]
        return None

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.arraydata[index.row()][index.column()]
