#! /usr/bin/python2.7
import math
import os
import random
import re
import sys

####################################################################
# hackerrank.com: Hash Table: two strings"
# input: s1 = 'hello', s2 = 'world'
# output: YES
# input: s1 = 'hi', s2 = 'world'
# output: NO

class soluTion(object):
    def TwoStrings(self, s1, s2):
        s1List = list(s1)
        s2List = list(s2)

        lens1 = len(s1List)
        lens2 = len(s2List)
        hashTable = {}

        for ii in s1List:
            if ii not in hashTable:
                hashTable[ii] = 1
            else:
                hashTable[ii] += 1

        count = 0
        for kk in s2List:
            if kk in hashTable:
                count += 1
        if count:
            return 'YES'
        else:
            return 'NO'


s1 = 'hello'
s2 = 'world'
#s1 = 'hi'
#s2 = 'world'

a = soluTion()
rst = a.TwoStrings(s1, s2)
print(rst)



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
