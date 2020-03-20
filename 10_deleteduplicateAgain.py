#! /usr/bin/python2.7
######################################################
## Try-again with James
## Description : Given a sorted array nums, remove the duplicates such that each element appear only once and return the new length.
## Date : 03/17/2020
## input: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
## output: 0 1 2 3 4
## Length = 5
######################################################
class   soluTion(object):
    def removeDup(self, arrayInpout):
        lenGth = len(arrayInpout)
        start = 0
        end = lenGth - 1
        count = 0
        result = []
        for i in range(lenGth):
            if not arrayInpout[i] in result:
                result.append(arrayInpout[i])
        return result

arrayIn = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
arrayIn = "adfbdfgggasdf"
print(arrayIn)
a=soluTion()
rst = a.removeDup(arrayIn)
print(rst)

