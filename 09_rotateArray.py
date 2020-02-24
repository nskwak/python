#! /usr/bin/python2.7
#'''
#####################################################################
# function: LeetCode:Easy 189. Rotate Array
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]

def RotateArr(arrayA, target):
    lenGth = len(arrayA)
    for k in range(target):
        tmp = arrayA[lenGth-1]
        for i in range(lenGth-1):
            arrayA[lenGth-1-i] = arrayA[lenGth-2-i]
        arrayA[0] = tmp
    return arrayA

a = [1,2,3,4,5,6,7]
target = 3
a = [-1, -100, 3, 99]
target = 2

print(a)
rst = RotateArr(a, target)
print(rst)
#####################################################################
#'''
