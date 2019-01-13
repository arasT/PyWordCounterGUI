from pywcgui_modules.utils import *

def analyseData(textData):
    """
        Analyse a text string and put statistic into a dict of word and their occurrence
        args :
            - textData (str): text to analyse
        Return : dict
    """

    from collections import Counter

    statDict = {}
    statDict["nbLines"] = len(textData.splitlines())
    statDict["nbChars"] = numberOfChar(textData.lower())

    # Removes non alphanumerical word
    word_list = stripNonAlphaNum(textData.lower())
    statDict["nbWords"] = len(word_list)

    # Count word and sort
    statDict["wordcount"] = Counter(word_list).most_common()
    return statDict

# Return filtered result according to arguments
def filterStatDict(statDict, length, times):
    """
        Filter the dict of word and their occurrence according to given args
        args :
        - length (int): word's length
        - times (str): number of times that the word occurs
        return : dict
    """

    filteredStatDict = {
        "nbLines": statDict["nbLines"],
        "nbWords": statDict["nbWords"],
        "nbChars": statDict["nbChars"],
    }
    filtredWordcountList = []

    for word, occur in statDict["wordcount"]:
        if len(word) >= length and occur >= times:
            filtredWordcountList.append((word, occur))

    filteredStatDict["wordcount"] = filtredWordcountList
    return filteredStatDict

def toTableFormat(filteredStatDict):
    """
        Format the filtered statistic dict into list that can be displayed into QT table
        arg :
            - filteredStatDict (dict): the dict to format
        return : list
    """

    tableFormat = []
    totalOccur = sum(occur for word, occur in filteredStatDict["wordcount"])

    # Filtered result holds data
    if len(filteredStatDict["wordcount"]) > 0:
        for word, occur in filteredStatDict["wordcount"]:
            currentRow = [word, occur, round(float(occur * 100)/totalOccur, 2)]
            tableFormat.append(currentRow)

    tableFormat.append([" ", " ", " "])
    tableFormat.append(["Number of lines", filteredStatDict["nbLines"], ""])
    tableFormat.append(["Number of words", filteredStatDict["nbWords"], ""])
    tableFormat.append(["Number of characters", filteredStatDict["nbChars"], ""])

    return tableFormat
