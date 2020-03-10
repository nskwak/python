#! /usr/bin/python2.7
#####################################################################
# function: LeetCode:Easy 9. Palindrome Number
# Input: 121
# Output: true
#
# Input: -121
# Output: false

class soluTion(object):
    def palindromeChk(self, inPut):
        orgInput = inPut
        lenGth = len(inPut)
        for i in range(0, lenGth/2):
            tmp = inPut[i]
            inPut[i] = inPut[lenGth-1-i]
            inPut[lenGth - 1 - i] = tmp
        return inPut

#inNum = -123
#inNumStr = str(inNum)           #convert from number to string -> "-123"
#inNumStrList = list(inNumStr)   #convert form string to char array list -> '-', '1', '2', '3'
#inStr = inNumStrList

inStr = 'abcd'
inStrList = list(inStr)

print("inStr: ", inStr)
a = soluTion()
rst = a.palindromeChk(inStrList)

lenGth_rst = len(rst)
stringVal = ""
for i in rst:
    stringVal += i

print(inStr, stringVal)
if(inStr == stringVal):
    print("palindrome")
else:
    print("NOT palindrome")

print("=============================================================")
print("================ test again for interview ===================")
def palendrom(arrayA):
    lenGth = len(arrayA)

    for i in range(lenGth/2):
        tmp = arrayA[i]
        arrayA[i] = arrayA[lenGth-1-i]
        arrayA[lenGth - 1 - i] = tmp
    return arrayA


a = "abcde"
b = list(a)

rst = palendrom(b)
print("rst= ", rst)

result = ""
for i in rst:
    result += i

print("result= ", result)

if result == a:
    print("Palendrom")
else:
    print("Not Palendrom")

