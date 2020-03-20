#! /usr/bin/python2.7
######################################################
## Function: Longest Common Prefix
## Description : Finds the longest common prefix of strings given in an array.
## Date : 03/18/2020
## input: ["flower","flow","flight"]
## output: "fl"
######################################################

class   soluTion(object):
    '''
    def FindLongest(self, arrayInpout):
        print(len(arrayInpout[0]), len(arrayInpout[1]), len(arrayInpout[2]), len(arrayInpout))
        lenGth = len(arrayInpout[0])
        result = ''
        for i in range(lenGth):
            for jj in range(1, len(arrayInpout)):
                if arrayInpout[0][i] != arrayInpout[jj][i]:
                    return result
            result = result + arrayInpout[0][i]
        return result
    '''

    def FindLongest(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()     #["flower", "flow", "flight"] => ["flower", "flow", "flight"]
        print("sorted", strs)
        res = ''
        for i in xrange(len(strs[0])):
            print(strs[-1][i], strs[0][i])
            if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res


arrayIn = ["flower", "flow", "flight"]
arrayIn = ["abced", "abe", "aaz"]
print("Input: ", arrayIn)
a=soluTion()
rst = a.FindLongest(arrayIn)
print(rst)

