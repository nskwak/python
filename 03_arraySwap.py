#! /usr/bin/python2.7

#'''
#####################################################################
# reverse string or string in list
def reverseNumInArr(in_N):
    lenGth = len(in_N)
    for i in range(0, lenGth/2):
        tmp = in_N[i]
        in_N[i] = in_N[lenGth-1-i]
        in_N[lenGth - 1 - i] = tmp
    return in_N

a = 'abcde'
a = list(a)
a = ['abcdef']
a = list(a[0])
rst = reverseNumInArr(a)
print(rst)

new = ""
for i in rst:
    new = new + i
print(new)
#####################################################################
#'''

'''
#####################################################################
# reverse Number or char in array
def reverseNumInArr(in_N):
    lenGth = len(in_N)
    for i in range(0, lenGth/2):
        tmp = in_N[i]
        in_N[i] = in_N[lenGth-1-i]
        in_N[lenGth - 1 - i] = tmp
    return in_N

a=[1,2,3,4,5,6]
a=[1,2,3,4,5]
a=['a', 'b', 'c', 'd', 'e', 'f']
a=['a', 'b', 'c', 'd', 'e']
rst = reverseNumInArr(a)
print(rst)
#####################################################################
'''

'''
#####################################################################
# reverse Number 
def reverseNum(in_N):
    siGned = 0
    if (in_N < 0):
        in_N = in_N * (-1)
        siGned = 1
    arr = []
    while True:
        rem = in_N % 10
        arr.append(rem)
        in_N = in_N - rem
        in_N /= 10
        #print(arr)
        if(in_N == 0):
            break
    print("arr:", arr, len(arr))
    raTio = len(arr)
    returnVal = 0
    for i in range(0, raTio):
        returnVal += arr[i] * 10 **(raTio - 1 -i)
    if(siGned == 1):
        returnVal *= (-1)
    return returnVal

#a=-123
rst = reverseNum(-123)
print(rst)
#####################################################################
'''

'''
#####################################################################
# function: LeetCode:Easy 7. Reverse Integer
# Input: 123
# Output: 321
# 
# Input: -123
# Output: -321
# 
# Input: 120
# Output: 21

class soluTion(object):
    def reverseNum(self, x):
        siGned = 0
        arr = []
        if (x < 0):
            x = x * (-1)
            siGned = 1
        while True:
            rem = x % 10
            arr.append(rem)
            x = x - rem
            x /= 10
            print(arr)
            if x == 0:
                break
        print(arr, len(arr))
        raTio = len(arr)
        reTurnVal = 0
        for i in range(0, raTio):
            reTurnVal += arr[i] * 10**(raTio - 1 - i)

        if (siGned == 1):
            reTurnVal *= (-1)

        return reTurnVal

a = soluTion()
rst = a.reverseNum(-123)
print(rst)
#####################################################################
'''
