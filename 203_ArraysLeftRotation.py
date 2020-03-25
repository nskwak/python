#! /usr/bin/python2.7
#'''
####################################################################
# hackerrank.com: Arrays: Left Rotation
# a = [1,2,3,4,5,6,7]
# target = 4
# output = [5,6,7,1,2,3,4]

def RotateRightArr(arrayA, target):
    lenGth = len(arrayA)
    for k in range(target):
        tmp = arrayA[lenGth-1]
        for i in range(lenGth-1):
            arrayA[lenGth-1-i] = arrayA[lenGth-2-i]
            #print(i, arrayA[lenGth-1-i], arrayA[lenGth-2-i])
        #print("=======================")
        arrayA[0] = tmp
    return arrayA

def RotateLeftArr(arrayA, target):      #O(n^2)
    lenGth = len(arrayA)
    loopcnt = 0
    for k in range(target):
        tmp = arrayA[0]
        for i in range(lenGth-1):
            arrayA[i] = arrayA[i+1]
            loopcnt += 1
            #print(i, arrayA[i], arrayA[i+1])
        #print("=======================")
        arrayA[lenGth-1] = tmp
    return arrayA, loopcnt

def RotateLeftArr111(arrayA, target):       #O(n)
    lenGth = len(arrayA)
    rotatedArr = [0 for i in range(lenGth)]
    rotatedArrIndex = target
    i = 0
    loopcnt = 0
    while(rotatedArrIndex < lenGth):
        rotatedArr[i] = arrayA[rotatedArrIndex]
        i += 1
        rotatedArrIndex += 1
        loopcnt += 1

    rotatedArrIndex = 0
    while(rotatedArrIndex < target):
        rotatedArr[i] = arrayA[rotatedArrIndex]
        i += 1
        rotatedArrIndex += 1
        loopcnt += 1
    return rotatedArr, loopcnt


a = [1,2,3,4,5,6,7]
target = 4
#a = [-1, -100, 3, 99]
#target = 2

print(a)
rst = RotateRightArr(a, target)
print("rotate array right to ", target, "   ", rst)

print("########################################################")
a = [1,2,3,4,5,6,7]
target = 4
rst = RotateLeftArr(a, target)
print("rotate array left to ", target, "   ", rst)

print("########################################################")
a = [1,2,3,4,5,6,7]
target = 4
rst = RotateLeftArr111(a, target)
print("rotate array left to ", target, "   ", rst)
#####################################################################
#'''
