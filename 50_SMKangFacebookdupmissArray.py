#! /usr/bin/python2.7
#####################################################################
# function: LeetCode:Easy 9. Palindrome Number
# https://medium.com/@sarahelson81/top-15-interview-questions-for-test-automation-engineers-e6c20842910
# Question 6
# you're given two sorted linked lists. Merge them
print("====================== Question 6 ===========================")
def sortArray(arrayA, arrayB, lenGthA, lenGthB):
    k = lenGthA + lenGthB - 1
    i = lenGthA - 1
    j = lenGthB - 1

    for ii in range(i, k):
        arrayA.append(0)

    while(i>=0 and j>=0):
        if (arrayA[i] > arrayB[j]):
            arrayA[k] = arrayA[i]
            k -= 1
            i -= 1
        else:
            arrayA[k] = arrayB[j]
            k -= 1
            j -= 1
    return arrayA

a = [1, 3, 4, 6, 8, 12, 86]
b = [5, 10]

lenA = len(a)
lenB = len(b)
rst = sortArray(a, b, lenA, lenB)
print(rst)
