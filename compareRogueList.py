#!/usr/bin/python3
import sys
import re
from collections import Counter
import re
#text = 'The quick brown\nfox jumps*over the lazy dog.'
#print(re.split('; |, |\*|\n',text))

def parseFile(fileName):
    with open(fileName,"r") as f:
        output = []
        for line in f:
            entry = re.split(' |:|,|\"|\.|\n',line)
            #entry = "A"
            #print("aaa")
            #entry1 = line.strip(',"\n')
            #print(''.join(entry1))
            #entry2 = entry1.split(':.')
            #print(''.join(entry2))
            output.append(''.join(entry))
        print(output)
    return output

def commonItems(list1,list2):
    common=[]
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                #print('found:')
                #print(item1)
                common.append(item1)
                break
    return common
def report(list1,list2,common,fileName):
    with open(fileName,"w") as f:
        f.write('#######Common Rogue AP between CMX and WLC :  ')
        f.write(len(common).__str__())
        f.write('\n')
        f.write('\n'.join(common))
        f.write('\n')

        wlcNot = []
        # find which is not in CMX
        for item in list2:
            if item not in common:
                wlcNot.append(item)
        f.write('########rogue AP in WLC list but not in common:  ')
        f.write(len(wlcNot).__str__())
        f.write('\n')
        f.write('\n'.join(wlcNot))
        f.write('\n')


        #find which is not in CMX
        cmxNot=[]
        for item in list1:
            if item not in common:
                cmxNot.append(item)

        f.write("########rogue AP in CMX list but not in common:  ")
        f.write(len(cmxNot).__str__())
        f.write('\n')
        f.write('\n'.join(cmxNot))

    return None
CMX_Rogue_APs = "/Users/vintran2/Downloads/CMX_Rogue_APs.txt"
WLC_Rogue_APs = "/Users/vintran2/Downloads/WLC_Rogue_APs.txt"

list1 = parseFile(CMX_Rogue_APs)
list2 = parseFile(WLC_Rogue_APs)
#print(list2)
common = commonItems(list2,list1)
#print(common)
reportFile="/Users/vintran2/Downloads/Rogue_Report.txt"
report(list1,list2,common, reportFile)
