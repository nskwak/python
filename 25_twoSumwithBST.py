#! /usr/bin/python2.7
# function: LeetCode:Easy 1. Two Sum
# Input: [2, 3, 7, 11, 13], target=9
# Output: [0, 2]
# a = [2, 3, 5, 7, 8, 9, 10, 11, 14, 15, 17, 20]
# a = [2, 14, 15, 3, 5, 10, 7, 8, 9, 11, 17, 20]
# target = 37
# output =

def sortNum(arrayN):
    lenGth = len(arrayN)
    loopcnt = 0
    for i in range(lenGth):
        for j in range(i):
            loopcnt += 1
            if(arrayN[j]>arrayN[i]):
                tmp = arrayN[j]
                arrayN[j] = arrayN[i]
                arrayN[i] = tmp
    print("loopcnt : %d", loopcnt)
    return arrayN

def twoSumOn(arrayN, target):
    lenGth = len(arrayN) - 1
    start = 0
    loopcnt = 0
    while(lenGth > start):
        loopcnt += 1
        if ((a[start] + a[lenGth]) == target):
            print("loopcnt : %d", loopcnt)
            return start, lenGth
        elif ((a[start] + a[lenGth]) > target):
            lenGth -= 1
        else:
            start += 1

def twoSumOnn(arrayN, target):
    lenGth = len(arrayN)
    i = 0
    j = 1
    loopcnt = 0
    for i in range(lenGth):
        for j in range(lenGth):
            loopcnt += 1
            #print("i, j", i, j)
            if((a[i]+a[j])==target):
                print("loopcnt : %d", loopcnt)
                return i, j

a = [2, 3, 5, 7, 8, 9, 10, 11, 14, 15, 17, 20]
a = [2, 14, 15, 3, 5, 10, 7, 8, 9, 11, 17, 20]
a = [2, 7, 11, 15]
target = 37
target = 9

print("=========================================")
print("============ twoSumO(n) =================")
a = sortNum(a)
print(a)
rst = twoSumOn(a, target)
print(rst)

print("=========================================")
print("============ twoSumO(n^2) ===============")
rst = twoSumOnn(a, target)
print(rst)