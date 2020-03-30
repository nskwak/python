#! /usr/bin/python2.7
import math
import os
import random
import re
import sys

#################################################################################
# inoput: 100_regression_Mod1.log
# 2020-03-10 09:20:24,807 INFO     regression_nvme_waive_skip.py:63: - localhost.localdomain :: 01. admin_001_abort_test.py                        : PASS (15.15 Sec)
# output: 100_regression_Mod1.out
# 01.  admin_001_abort_test.py                    : PASS
#################################################################################
inFile  = open("100_regression_Mod1.log", 'r')
outFile = open("100_regression_Mod1.txt", 'w')
linelength = 1
while(linelength != 0):
    inVar1 = inFile.readline()
    linelength = len(inVar1)
    if(linelength == 0):
        break
    inVar1 = inVar1.rstrip()
    inVar1List = inVar1.split(' ')
    lenGth = len(inVar1List)
    firstHit = inVar1.find('INFO')
    secondHit = inVar1.find('localhost')
    thirdHit = inVar1.find(':')

    if(firstHit > -1) & (secondHit > -1) & (lenGth > 20):   #if readline includes "INFO" and "localhost"
        inVar1ListnoSpace = []
        for a in inVar1List:
            if a is not '':
                inVar1ListnoSpace.append(a)
        #print(inVar1ListnoSpace)
        fmtinfo = "{0: <4} {1: <42} {2} {3}"
        #print(fmtinfo.format(inVar1ListnoSpace[2], inVar1ListnoSpace[7]))
        outFile.write(fmtinfo.format(inVar1ListnoSpace[7], inVar1ListnoSpace[8], inVar1ListnoSpace[9], inVar1ListnoSpace[10]) + "\n")
        #outFile.write(inVar1ListnoSpace[2] + ' ' + inVar1ListnoSpace[7] + "\n")
        #print(fmtinfo.format(inVar1ListnoSpace[9], inVar1ListnoSpace[10]))
print(inVar1ListnoSpace)

'''    
####################################################################################
        fmtinfo = "{0: >20}: {1} "
        print(fmtinfo.format(inVar1ListnoSpace[2], inVar1ListnoSpace[7]))
        outFile.write(fmtinfo.format(inVar1ListnoSpace[2], inVar1ListnoSpace[7]) + "\n")
####################################################################################
def AppendFile(text, filename):
    """Equivalent to >> in BASH, append a line to a text file."""
    with open(filename, "a") as f:
        f.write(text)
        f.write("\n")

####################################################################################
    descfmt = "{0:" + str(maxlen) + "}"
    resfmt = "{1: >8} {2: >9} {3: >8}"
    fmtstr = descfmt + " " + resfmt

####################################################################################
    print("ezFio test parameters:\n")
    fmtinfo = "{0: >20}: {1}"
    print(fmtinfo.format("Drive", str(physDriveTxt)))
    print(fmtinfo.format("Model", str(model)))

'''
