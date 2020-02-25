#! /usr/bin/python2.7
#####################################################################
# https://medium.com/@sarahelson81/top-15-interview-questions-for-test-automation-engineers-e6c20842910
# Question 14
# find maximum and second maximum number in an array of integers using your favorite programming language
print("====================== Question 14 ===========================")
print("================== this is correct answer ====================")
def findmaxnuminArray(arrayA, lenGthA):
    if(lenGthA < 2):
        print("invalid input")
        return
    first = second = -2147483648
    for ii in range(lenGthA):
        if arrayA[ii] > first:
            second = first
            first = arrayA[ii]
        elif arrayA[ii] > second and arrayA[ii] != first:
            second = arrayA[ii]
    return first, second

a = [1, 3, 4, 6, 67, 2, 8, 12, 86]

lenA = len(a)
rst = findmaxnuminArray(a, lenA)
print(rst)


print("====================== Question 14 ===========================")

def findmaxnuminArray(arrayA, lenGthA):
    for ii in range(lenGthA):
        for jj in range(ii):
            if (arrayA[jj] > arrayA[ii]):
                tmp = arrayA[jj]
                arrayA[jj] = arrayA[ii]
                arrayA[ii] = tmp
    return arrayA[lenGthA-1], arrayA[lenGthA-2]

a = [1, 3, 4, 6, 67, 2, 8, 12, 86]
lenA = len(a)
rst = findmaxnuminArray(a, lenA)
print(rst)
