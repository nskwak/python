#! /usr/bin/python2.7
######################################################
## Try-again with James
## Function: Palindrome Number
## Description : Given an integer, determines whether it reads the same way forwards as it does backwards
## Date : 03/17/2020
## input: -1456
## output: FALSE (-1456 is not the same as 6541-)
######################################################
class   soluTion(object):
    def chkPalindrome(self, arrayInpout):
        lenGth = len(arrayInpout)
        start = 0
        end = lenGth - 1
        count = 0
        while(end > start):
            count += 1
            if(arrayInpout[start] != arrayInpout[end]):
                return False, count
            else:
                start += 1
                end -= 1
        return True, count

arrayIn = "1221"
print(arrayIn)
arrayIn = list(arrayIn)
a=soluTion()
rst = a.chkPalindrome(arrayIn)
print(rst)

