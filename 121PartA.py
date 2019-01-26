#!/usr/bin/python3
#test run success with python3.6.6
""" Name: Vu Quoc Tran
    ID:   48894667
    CS 121 - Project 1  """

"""Note: Actually Part A and Part B code in the same file, it's  easy to do B by import A 
   but I dont, because TA might test them separately in different directories """

"""
Algorithm: Pseudocode
Part A
Read input file
Tokenize the file, ignore the capital, + number of appearance
Sorting by highest frequency (take O(nlgn) )
Print the list out
Complexity: O(nlgn) with n is the number of tokens

Part B: Take two lists of sorted, find the common items
Using the built-in set.intersection()
While (X=traverse(list 1) || Y=traverse (list2))
  if X==Y //this is the common the store it
  else X > Y then traverse down list 2
  else Y > X then traverse down list 1
Complexity is O(n) but sorting takes O(nlgn)
Thus, total complexity: O(nlgn) with n is the number of tokens
"""

import sys
import re
from collections import Counter

def getTokensList(fileName):
    """ Convert file name text contents into sorted list of tokens in alphabetically
        Reading lines in file: O(n)
        Sorting token list: O(nlgn)
        Thus, complexity: O(nlgn)    """
    tokensList = []
    pattern = re.compile('[a-z0-9]+', re.IGNORECASE)
    with open(fileName, "r") as f:                  #todo: multi-threading
        for line in f:
            tokenLine = pattern.findall(line.lower())
            tokensList += tokenLine
    #tokensList.sort(key=str.lower)
    #print(tokensList)
    return sorted(tokensList)       #to ensure later sorted(dictList) return descending by value and ascending by key

def buildDict(fileName):
    """ Returns a list of pairs (key,value)
        [("keys" -> "number of appearance of the key")] and sorted by the highest appearance
        Complexity: O(nlgn)    """
    tokenList = getTokensList(fileName)
    dictList = Counter() #faster
    for token in tokenList:
        dictList[token] += 1
    return dictList

def intersection2files(fileName1, fileName2):
    """ Return the intersection of same tokens of 2 files
        Complexity: O(nlgn) """
    tokenSet1 = set(getTokensList(fileName1))       #having another version use multi-processing for >100MB input file
    tokenSet2 = set(getTokensList(fileName2))
    interSet = tokenSet1.intersection(tokenSet2)
    return interSet

def Run():
    #Sanity check on inputs
    if not (2 <= len(sys.argv) <= 3):
        print("Part A Usage: " + sys.argv[0] + " [file]")
        print("Part B Usage: " + sys.argv[0] + " [file1] [file2]")
        exit(1)
    try:
        if len(sys.argv) == 2:      #Part A:
            #print("Part A: tokens - number of appearance are:")
            dictList = buildDict(sys.argv[1])
            sortedDict = sorted(dictList.items(), key=lambda j: j[1], reverse=True)
            for (k, v) in sortedDict:
                print(k, "\t", v)
            #print("\n")
        if len(sys.argv) == 3:      #Part B:
            interSet = intersection2files(sys.argv[1], sys.argv[2])
            #print("Part B: The same tokens in both files are: ")
            # for i in interSet:
            #     print(i)
            # print("Total of intersect tokens: ", len(interSet), "\n")
            print(len(interSet))
        exit(0)
    except Exception:
        print("File not found or other error exception. Program exit!")
        exit(1)

if __name__ == '__main__':
    Run()

