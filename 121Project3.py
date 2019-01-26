#!/usr/bin/python3
# @Vu Tran
""" Team 55
    Vu Tran - 48894667
    Anas ??
    Hoang - 20843397
    CS 121 - Project 3  """

""" Objective: 
    Build INDEX table from 37,497 files
    Parsing for keywords
    """

""" Data structure:
    INDEX is a dict= {keyword:(set of (docID,frequency)), ...}, works as main database
    docID = foldNum * 1000 + location file number of that folder, ex: 34/156 => docID = 34156
    """

""" Algorithm:
    For each docID do
        IF a "keyword" found not existing in the INDEX
            adding it to INDEX[keys]
            adding docID to the set of that "keywords" in INDEX
        ELSE
            adding docID to the set of that "keywords" in INDEX
    Store INDEX database on a file
    """

""" TODO Improving Performance:
        1. Applying only to html content (vincent)
        2. Filtering stopword   (vincent)
        3. Applying compression methods for saving INDEX (Hoang)
        4. Applying Stemming and lemmatization (Anas)
        5. Function to calculate df-idf from docID (Hoang)
        6. Implement ranking single keyword query (Anas)
        7. Implement ranking PHRASE query (Anas or Hoang, should be the same person doing task 6)
        8. Implement parallel processing for performance (optional, vincent)
        9. Implement GUI (optional, Anas)
        10.Design (vincent)  
        11.Managing the project (vincent)
    Reference: https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html
    """
"""" Answer query:
    """

""" Reference: https://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html
             : https://arxiv.org/pdf/1208.6109.pdf => wordlength < 20 ?
    """

import os, sys, math, json, io
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords  # Get the common english stopwords
from bs4 import BeautifulSoup, SoupStrainer  # Get content from html files
from pathlib import Path
from operator import itemgetter
from nltk.stem import PorterStemmer  # https://www.datacamp.com/community/tutorials/stemming-lemmatization-python

INDEX = dict()  # INDEX = {keyword: {set of (docID, tf-idf score)}}
posting_list = dict()  # = { 'keyword' : (doc1,doc2, ....) }
docLocation = dict()  # = { "docID" : path}
NUM_OF_FOLDERS = 75  # 0-74, 0-499
NUM_OF_FILES_PER_FOLDER = 50  # 500        #0-74, 0-499
MAXWORDLENGTH = 20
MINWORDLENGTH = 2
TOTAL_NUM_OF_DOC = 37497  # total documents


def buildINDEX(rootFolder):
    # 0-74, 0-499
    # Build docID - filename mapping
    for i in range(0, NUM_OF_FOLDERS):
        for j in range(0, NUM_OF_FILES_PER_FOLDER):
            filePath = rootFolder + "/" + str(i) + "/" + str(j)  # WEBPAGES_RAW/0/12
            docID = i * 1000 + j
            docLocation[str(docID)] = filePath
    # print (docLocation)

    # Traverse each file docID and processing
    for docID in docLocation:
        try:
            buildPostingList(docID)
            # print("processing docID: " + docID)
        except ValueError as e:
            print(e, "<---------line 86")
            continue

    return None


# Hoang modified this fuction to print the posting list without frequency at the beginning
def buildPostingList(docID):
    tokenList, temp_set = getTokensList(docLocation[docID])
    for keyword in tokenList:
        # todo here
        if keyword not in posting_list:
            tmpSet = set()
            tmpSet.add(docID)
            posting_list[keyword] = tmpSet  # posting_list = {keyword : (doc1, doc2, ...)}
        else:
            posting_list[keyword].add(docID)
    return None


# Hoang added code ----------------START-------------------------
def build_list_with_IDF_score(tokenList):
    count = 0
    for keyword in tokenList:
        tokenList[keyword] = math.log(TOTAL_NUM_OF_DOC / len(tokenList[keyword]), 10)
        # print("Calculating idf keyword: " + keyword + " - keys left: " + str(len(tokenList)-count))
        count += 1
    return tokenList


def updating_INDEX():
    idf_score_list = build_list_with_IDF_score(posting_list)

    # Traverse each file docID and processing
    for docID in docLocation:
        try:
            processOneDoc(docID, idf_score_list)
            print("Populating complete INDEX file: " + docID)
        except:
            continue
    return None


def processOneDoc(docID, idf_score_list):
    dictList, title_list = buildDict(docLocation[docID])  # dictList is a dict of (keyword : freq)
    for keyword in dictList:
        # todo here
        tmpTuple = (docID, int((1 + math.log(dictList[keyword], 10)) * idf_score_list[keyword] * 100),
                    title_list[keyword])  # Calculate tf-idf score

        if keyword not in INDEX:
            tmpSet = list()
            tmpSet.append(tmpTuple)
            INDEX[keyword] = tmpSet  # INDEX = {keyword: {set of (docID, if-tdf score)}}
        else:
            INDEX[keyword].append(tmpTuple)
            INDEX[keyword].sort(key=itemgetter(1, 2), reverse=True)


# Hoang added code -------------------------------------- END-------------------------

def runQuery(searchKeyword, numOfDocs):
    if searchKeyword in INDEX:
        tmpSet = INDEX[searchKeyword]  # = {(docID, freq), ...}
        sortedList = sorted(tmpSet, key=lambda item: item[1], reverse=True)
        # print ("Query result of " + str(searchKeyword))
        # for i in sortedList[0:numOfDocs]:
        #     print(i)
        if numOfDocs < len(sortedList):
            queryResult = sortedList[0:numOfDocs]
        else:
            queryResult = sortedList
    else:
        queryResult = set()
    return queryResult  # Return a list of (docID,freq)


def locateTSV(docID, fileName):  # For milestone 1, I doing with tsv file, todo with json library later on
    docDirNum, docFileNum = divmod(docID, 1000)
    docTag = str(docDirNum) + "/" + str(docFileNum)
    # print(docTag)
    foundURL = "URL Not Found"
    try:
        with open(fileName, "r") as f:  # todo: multi-threading
            for line in f:
                pattern = line.split('\t', maxsplit=2)
                for pat in pattern:
                    # print(pat)
                    if pat == docTag and len(pattern) > 1:
                        foundURL = pattern[1]
    except:
        foundURL = "Error-Finding-URL"
    return foundURL


def writeINDEXToFile():
    try:
        with open("./output/5pm.txt", "w", encoding="utf-8") as f:
            for keyword in INDEX:
                f.write(keyword)
                f.write('\t')
                f.write(str(INDEX[keyword]))
                f.write('\n')
    except ValueError as e:
        print(e, "<------------- line 184")


# Hoang added code ---------------START------------------
def writeJSONFile():
    with open("./output/5pm.json", 'w', encoding="utf-8") as file:
        json.dump(INDEX, file, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


# Hoang added code ---------------END------------------

def reportMilestone1():
    # Build & store INDEX database
    # Need to change / to \ if using WINDOW
    if sys.platform.startswith('win32'):
        slash = "\\"
    else:
        slash = "/"

    rootFolderPath = os.getcwd() + slash + "WEBPAGES_RAW"
    TSVFile = rootFolderPath + slash + "bookkeeping.tsv"
    indexFilePath = rootFolderPath + slash + "INDEX"

    buildINDEX(rootFolderPath)
    updating_INDEX()  # Hoang added code

    writeJSONFile()  # Hoang added code

    writeINDEXToFile()

    # # Query list
    # queryList = ['informatics', 'mondego', 'irvine', 'artificial', 'computer']
    # stemList(queryList)
    # print(queryList)
    # queryReturn = list()
    # numOfReturn = 10
    # for query in queryList:
    #     print("Query result of " + str(query) + " :")
    #     result = runQuery(query, numOfReturn)
    #     for docIDItem in result:
    #         foundURL = locateTSV(int(docIDItem[0]), TSVFile)
    #         queryReturn.append((docIDItem[0], foundURL))
    #         docDirNum, docFileNum = divmod(int(docIDItem[0]), 1000)
    #         docTag = str(docDirNum) + "/" + str(docFileNum)
    #         print("\tDocID " + str(docTag) + " : " + str(foundURL))
    #     # print(queryReturn)
    # return None


##################### Text Processing #################################################################
def getTokensList(fileName):
    """ Convert file name text contents into sorted list of tokens in alphabetically
        Reading lines in file: O(n)
        Sorting token list: O(nlgn)
        Thus, complexity: O(nlgn)    """
    tokensList = []
    pattern = re.compile('[a-z0-9]+', re.IGNORECASE)
    stopWords = set(stopwords.words('english'))  # Init here for the performance

    # https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=SoupStrainer
    # https://www.w3schools.com/html/html_intro.asp
    # parsingTags = ['b','p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'title']
    try:
        tokensList2 = []
        with open(fileName, "r", encoding='utf8') as f:  # todo: multi-threading
            soupObj = BeautifulSoup(f, "html.parser")  # parse every tag in a html

            vipList = [i.get_text(" ") for i in soupObj.find_all(['h1', 'h2', 'h3', 'b'])]
            if (soupObj.title != None):
                vipList.append(soupObj.title.text)
            vipString = "".join(vipList)

            for script in soupObj(["head", "script", "style"]):
                script.decompose()

            content = soupObj.get_text(" ")
            tokenLine = pattern.findall(content.lower())
            tokensList = filterPattern(tokenLine, stopWords)

            tokenLine2 = pattern.findall(vipString.lower())  # Tokenize
            tokensList2 = filterPattern(tokenLine2, stopWords)  # stopWord + stemming

    except UnicodeEncodeError as e:
        print(e, "<---- 253")

    return sorted(tokensList), tokensList2


def buildDict(fileName):
    """ Returns a list of pairs (key,value)
        [("keys" -> "number of appearance of the key")] and sorted by the highest appearance
        Complexity: O(nlgn)    """

    tokenList, headersList = getTokensList(fileName)
    dictList = Counter()  # faster
    headerDict = Counter()

    for token in tokenList:
        dictList[token] += 1

    for token in headersList:
        headerDict[token] += 1

    return dictList, headerDict


def filterPattern(tokenList, stopWords):  # Applying all possible rules to filtering out non-sense keywords
    filteredList = []
    Porter = PorterStemmer()
    for pattern in tokenList:
        selectPattern = True
        if (re.compile('^[0-9].*', re.IGNORECASE)).match(str(pattern)) \
                or (re.compile('^[0-9]+', re.IGNORECASE)).match(str(pattern)) \
                or (pattern in stopWords) \
                or (len(str(pattern)) > MAXWORDLENGTH) \
                or (len(str(pattern)) <= MINWORDLENGTH):
            selectPattern = False

        if selectPattern:
            stemPattern = Porter.stem(pattern)  # stemming it before adding
            filteredList.append(stemPattern)
            # filteredList.append(pattern)

    return filteredList


def stemList(listOfTokens):  # Applying stemming rules for each keywords
    Porter = PorterStemmer()
    for i in range(len(listOfTokens)):
        # applying the stemmer of each item in the list
        listOfTokens[i] = Porter.stem(listOfTokens[i])
    return None


def main():
    reportMilestone1()


main()

##################################################
# for testing/debug performance only
# https://www.clips.uantwerpen.be/tutorials/python-performance-optimization
# def profile(function, *args, **kwargs):
#     """ Returns performance statistics (as a string) for the given function.
#     """
#
#     def _run():
#         function(*args, **kwargs)
#
#     import cProfile as profile
#     import pstats
#     import os
#     import sys;
#     sys.modules['__main__'].__profile_run__ = _run
#     id = function.__name__ + '()'
#     profile.run('__profile_run__()', id)
#     p = pstats.Stats(id)
#     p.stream = open(id, 'w')
#     p.sort_stats('time').print_stats(20)
#     p.stream.close()
#     s = open(id).read()
#     os.remove(id)
#     return s
#
#
# ###################################################
#
# # Main()
# if __name__ == '__main__':
#     print(profile(Run))