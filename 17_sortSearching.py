#! /usr/bin/python2.7

#'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# find number in sorted array
# input = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16, 17,18,19,20]]
# find '5' -> output should be True
#####################################################################
print("===================================================================")
def searchElem(arrayA, key, M, N):
    roW = 0
    coL = N - 1
    print(arrayA[roW][coL])
    while (roW < M and coL >= 0):
        if (arrayA[roW][coL] == key):
            print(roW, coL)
            return True
        elif (arrayA[roW][coL] > key):
            coL = coL - 1
        else:
            roW = roW + 1
    return -1

a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16, 17,18,19,20]]
row = len(a)      # M = 4
col = len(a[0])   # N = 5
print(row, col)
rst = searchElem(a, 9, row, col)
print(rst)

#####################################################################
#'''


#'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# Given a sorted array of n integers that has been rotated an unknown number of times,
# give an O(log n) algorithm that finds an element in the array. you may assume that
# the array was originally sorted in increasing order.
# input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10,14], find '5' -> output should be 8
#####################################################################
print("===================================================================")
print("============ find number in unsorted/shifted array number =========")
def searchElement1(arrayA, key):
    lenGth = len(arrayA)
    start = 0
    end = lenGth - 1

    while (start <= end):
        m = (start + end) / 2
        if (key == arrayA[m]):
            return m
        elif (arrayA[start] <= arrayA[m]):
            if(key > arrayA[m]):
                start = m + 1
            elif (key >=arrayA[start]):
                end = m - 1
            else:
                start = m + 1
        elif (key < arrayA[m]):
            end = m - 1
        elif (key <= arrayA[end]):
            start = m + 1
        else:
            start = m + start
    return -1

a = [4, 5, 7, 10, 14, 15, 16, 19, 20, 25, 1, 3]
a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
a = [10, 14, 15, 16, 19, 20, 25, 1, 3, 4, 5, 7]
a = [25, 1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20]
a = [13, 25, 27, 35, 1, 3, 5, 7, 9]

findVal = 13
rst = searchElement1(a, findVal)
print("find number in unsorted/shifted array number", rst)

#####################################################################
#'''


#'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# find number in sorted array
# input = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25], find '5' -> output should be 3
#####################################################################
print("===================================================================")
def searchElement(arrayA, key):
    lenGth = len(arrayA)
    start = 0
    end = lenGth - 1

    while (start <= end):
        m = (start + end) / 2
        if (key == arrayA[m]):
            return m
        elif (arrayA[m] < key):
            start = m + 1
        else:
            end = m - 1
    return -1
#    0  1  2  3  4   5   6   7   8   9  10  11
a = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
target = 5
rst = searchElement(a, target)
print("target(%d) is located in a[%d]" %(target, rst))
#####################################################################
#'''

#'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.1
# you are given two sorted array, A and B, and A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order
# (1) append arrayB into arrayA (2) sort arrayA
# (2) compare from the end of arrayA, arrayB and save bigger one
#####################################################################
print("===================================================================")
print("======== (2) method ===============================================")
def mergeFunc(arrayA, arrayB, lenA, lenB):
    k = lenA + lenB -1
    iA = lenA - 1
    iB = lenB - 1
    for i in range(lenB):
        arrayA.append(0)
    print(arrayA)

    while ((iA >= 0) and (iB >= 0)):
        #print(iA, iB)
        if arrayA[iA] > arrayB[iB]:
            arrayA[k] = arrayA[iA]
            k = k - 1
            iA = iA - 1
        else:
            arrayA[k] = arrayB[iB]
            k = k - 1
            iB = iB - 1
    return arrayA

a = [1, 12, 13, 14, 17, 28, 110]
b = [22, 23]
lenGA = len(a)
lenGB = len(b)

rst = mergeFunc(a, b, lenGA, lenGB)
print(rst)


print("===================================================================")
print("======== (1) method ===============================================")

def mergeFunc(arrayA, arrayB, lenA, lenB):
    k = lenA + lenB -1
    iA = lenA - 1
    iB = lenB - 1
    result = a
    for i in range(lenB):
        result.append(arrayB[i])

    for i in range(k+1):
        #print(i)
        for j in range(i):
            #print(i,j)
            if arrayA[j] > arrayA[i]:
                tmp = arrayA[i]
                arrayA[i] = arrayA[j]
                arrayA[j] = tmp
    return result

a = [1, 12, 13, 14, 17, 28, 110]
b = [2, 23]
lenGA = len(a)
lenGB = len(b)

rst = mergeFunc(a, b, lenGA, lenGB)
print(rst)

#####################################################################
#'''
