#! /usr/bin/python2.7
import math
import os
import random
import re
import sys

####################################################################
# hackerrank.com: Hash Table: Two String
# Magzine = "give me one grand today night"
# target = 6
# Ransom Note = "give one grand today"
# target = 4
# output = Yes

class soluTion(object):
    def RandomNote(self, magazine, note):
        lenMazL = len(magazine)
        lenRanL = len(note)
        MagzinDict = {}

        for ii in range(lenMazL):
            if ii not in MagzinDict:
                tmp = {magazine[ii]: 0}
                MagzinDict.update(tmp)
            MagzinDict[magazine[ii]] += 1

        for kk in range(lenRanL):
            if note[kk] not in MagzinDict or MagzinDict[note[kk]] == 0:
                #print("No")
                return False
            else:
                MagzinDict[note[kk]] = MagzinDict[note[kk]] - 1
        #print("Yes")
        return True


#Magzin = "give me one grand today night"
#Ransom = "give one grand today"
Magzin = "ive got a lovely bunch of coconuts"
Ransom = "ive got some coconuts"
Magin = "two times three is not four"
Ransom = "two times two is four"
MagzinList = Magzin.split(' ')
RansomList = Ransom.split(' ')

a = soluTion()
rst = a.RandomNote(MagzinList, RansomList)
if rst:
    print("Yes")
else:
    print("No")
'''
Magzin = "give me one grand today night"
Ransom = "give one grand today"

lenMaz = len(Magzin)
lenRan = len(Ransom)

MagzinList = Magzin.split(' ')
RansomList = Ransom.split(' ')
lenMazL = len(MagzinList)
lenRanL = len(RansomList)
MagzinDict = {}

for ii in range(lenMazL):
    if ii not in MagzinDict:
        tmp = {MagzinList[ii]:0}
        MagzinDict.update(tmp)
    print(MagzinDict)
    MagzinDict[MagzinList[ii]] += 1
    print(MagzinDict)

for kk in range(lenRanL):
    if(MagzinDict[RansomList[kk]] > 0):
        MagzinDict[RansomList[kk]] = MagzinDict[RansomList[kk]] - 1
    else:
        print("No")
print("Yes")
'''
