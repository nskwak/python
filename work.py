#!/usr/bin/python2.7

#'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# find number in sorted array
# input = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16, 17,18,19,20]]
# find '5' -> output should be True
#####################################################################
def searchElem(arrayA, key, M, N):
    roW = 0
    coL = N - 1
    print(arrayA[roW][coL])
    while (roW < M and coL >= 0):
        if (arrayA[roW][coL] == key):
            return True
        elif (arrayA[roW][coL] > key):
            coL = coL - 1
        else:
            roW = roW + 1
    return -1

a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16, 17,18,19,20]]
row = len(a)      # M = 3
col = len(a[0])   # N = 5
rst = searchElem(a, 9, row, col)
print(rst)

#####################################################################
#'''

'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# find number in sorted array
# input = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25], find '5' -> output should be 3
#####################################################################
def searchString(arrayA, key):
    lenGth = len(arrayA)
    start = 0
    end = lenGth - 1
    print(lenGth)

    while (start <= end):
        m = (start + end) / 2
        if (arrayA[start] == key):
            return start
        #if (arrayA[m] == key):
        #    return m
        #while()
        start = start + 1
    return -1
#    0       1    2    3     4     5     6         7   8      9   10
a = ['', 'ball', '', 'ca', 'da', 'er', 'ft', 'gallse', '', 'hed', '']
rst = searchString(a, 'ball')
print(rst)

#####################################################################
'''

'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# find number in sorted array
# input = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25], find '5' -> output should be 3
#####################################################################
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

for i in range(0,30):
    rst = searchElement(a, i)
    if rst is -1:
        print("%2d is not in array a" % i)
    else:
        print("%2d is located in a[%d]" % (i, rst))
#####################################################################
'''


'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# Given a sorted array of n integers that has been rotated an unknown number of times,
# give an O(log n) algorithm that finds an element in the array. you may assume that
# the array was originally sorted in increasing order.
# input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10,14], find '5' -> output should be 8
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
#####################################################################
def pivotedBinarySearch(arr, n, key):       #array, length, key
    print("pivotedBinarySearch", n, key)
    pivot = findPivot(arr, 0, n - 1)
    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n - 1, key)
    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key)
    return binarySearch(arr, pivot + 1, n - 1, key)

def findPivot(arr, low, high):              #array, 0 ~ length-1
    print("findPivot", low, high)
    # base cases
    if high < low:
        return -1
    if high == low:
        return low
        # low + (high - low)/2;
    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        print("111111:")
        return findPivot(arr, low, mid - 1)
    print("222222:")
    return findPivot(arr, mid + 1, high)

def binarySearch(arr, low, high, key):
    print("binarySearch", low, high)
    if high < low:
        return -1
    # low + (high - low)/2;
    mid = int((low + high) / 2)
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key);
    return binarySearch(arr, low, (mid - 1), key);

a = [4, 5, 7, 10, 14, 15, 16, 19, 20, 25, 1, 3]
a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
a = [10, 14, 15, 16, 19, 20, 25, 1, 3, 4, 5, 7]
#a = [25, 1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20]
#a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(a)
key = 3
print("Index of the element is : ",  pivotedBinarySearch(a, n, key))
#####################################################################
'''



'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.3
# Given a sorted array of n integers that has been rotated an unknown number of times,
# give an O(log n) algorithm that finds an element in the array. you may assume that
# the array was originally sorted in increasing order.
# input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10,14], find '5' -> output should be 8
#####################################################################
def searchElement(arrayA, key):
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

rst = searchElement(a, 5)
print(rst)

#####################################################################
'''


'''
#####################################################################
# function: sort and searching
# Cracking code page 66, 9.1
# you are given two sorted array, A and B, and A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order
#####################################################################

def mergeFunc(arrayA, arrayB, lenA, lenB):
    k = lenA + lenB - 1
    i = lenA - 1
    j = lenB - 1

    for ii in range(i,k):
        arrayA.append(0)

    while((i >= 0) and (j >= 0)):
        if(arrayA[i] > arrayB[j]):
            arrayA[k] = arrayA[i]
            k = k - 1
            i = i - 1
        else:
            arrayA[k] = arrayB[j]
            k = k - 1
            j = j - 1
    return arrayA

a = [1, 12, 13, 14, 17, 28, 110]
b = [2, 23]
lenGA = len(a)
lenGB = len(b)

rst = mergeFunc(a, b, lenGA, lenGB)
print(rst)

#####################################################################
'''

'''
#####################################################################
# function: bit maipulation
# Cracking code page 58, 5.6
# problem 1) input: 31, 14 -> output: 2
# problem 2) b0 and b1 swapped, b2 and b3 are swapped
#####################################################################

def countXorValue(in_num):
    count = 0
    while(in_num):
        count += in_num & 1
        in_num >>= 1
    return count

def swapbit(x):
    return (((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1))

a = 31
b = 14

print(countXorValue(a^b))

c = 0x3
d = 0x2
print(c|d)
print(c&d)

e = 0x11111111
print(swapbit(e), hex(swapbit(e)))
#####################################################################
'''


'''
#####################################################################
# function: bit maipulation
# Cracking code page 58, 5.5
# input: 31, 14 -> output: 2
#####################################################################

def countXorValue(in_num):
    count = 0
    while(in_num):
        count += in_num & 1
        in_num >>= 1
    return count
a = 31
b = 14

print(countXorValue(a^b))
#####################################################################
'''

'''
#####################################################################
# function: bit maipulation
# Cracking code page 57, 5.1
# a)  N = 1024 (10000000000),
#     M = 19 (10011),
#     i = 2, j = 6
#     Output : 1100 (10001001100)
# b)  N = 1201 (10010110001)
#     M = 8 (1000)
#     i = 3, j = 6
#     Output: 1217 (10011000001)
#####################################################################

N = 0b10010110001       #1201
M = 0b1000              #8
i = 3
j = 6

print("1. N = ", N, bin(N))
capture_mask = (1 << i) - 1         #i = 3 -> capture_mask = 7 = 0b111
captured_bit = N & capture_mask     #captured_bit = 001
print("2. N = ", captured_bit, bin(captured_bit))

clear_mask = -1 << (j+1)            #j = 6 -> clear_mask =
cleared_bit = N & clear_mask        # N & 0000000
print("3. N = ", cleared_bit, bin(cleared_bit))

M <<= i
cleared_bit |= M
print("4. N | (M<<i) ", cleared_bit, bin(cleared_bit))

result = cleared_bit | captured_bit
print("5. N | captured_bit(& 111) ", result, bin(result))
#####################################################################
'''

'''
#####################################################################
# function: given sorted(increasing order) array, write an algorithm
# to create binary tree with minimal height
# BST : Binary Search Tree
# Cracking code page 54, 4.3
#            4
#      2           6
#   1     3     5     7
# 4 - 2 - 1 - 3 - 6 - 5 - 7
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if not arr:
        return None
    mid = len(arr) /2
    root = Node(arr[mid])
    print(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

def preOrder(node):
    if not node:
        return
    print node.data
    preOrder(node.left)
    preOrder(node.right)

# main routine
ArrayIn = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#ArrayIn = [1, 2, 3, 4, 5, 6, 7]
#ArrayIn = [1, 2, 3, 4, 5, 6]
#ArrayIn = [1, 2, 3]

print("============================")
root = sortedArrayToBST(ArrayIn)
print("============================")
preOrder(root)

#####################################################################
'''


'''
#####################################################################
# function: tree is balanced or not -#2
# Cracking code page 54, 4.1
#
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def minDepth(root):
    if root is None:
        return 0
    return 1 + min(minDepth(root.left), minDepth(root.right))

def isBalanced(root):
    return (maxDepth(root) - minDepth(root) < 1)

# main routine
root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
#root.left.left.left = Node(4)
#root.left.left.right = Node(4)
print("minDepth = ", minDepth(root))
print("maxDepth = ", maxDepth(root))

print("isBalanced = ", isBalanced(root))
#####################################################################
'''


'''
#####################################################################
# function: Find Minimum Depth of a Binary Tree -#1
# https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
#
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def minDepth(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0

        # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        return 1

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth(root.right) + 1

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1


# Driver Program
root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
print minDepth(root)
#####################################################################
'''

'''
#####################################################################
# function: lambda
x = lambda a : a+10
print(x(5))
#####################################################################
'''

'''
#####################################################################
# function: find how many same character in array.
class soluTion(object):
    def searchDuplicate(self, inputCharArr):
        lenGth = len(inputCharArr)
        res = []
        resdup ={}
        for inp in inputCharArr:
            if inp not in res:
                res.append(inp)
            else:
                if inp not in resdup:
                    tmp = {inp : 1}
                    resdup.update(tmp)
                else:
                    resdup[inp] += 1
        return resdup

in_arr = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'e']
a = soluTion()
print(in_arr)
rst = a.searchDuplicate(in_arr)
print(rst)

#####################################################################
'''

'''
#####################################################################
# function: sort array
# Input : [1, 4, 45, 6, 10, -8]
# Output: [-8, 1, 4, 6, 10, 45]

class soluTion(object):
    def sortArray(self, number):
        LenGth = len(number)
        for i in range(0, LenGth):
            for j in range(0, i):
                print("j=", j, " i=", i, number[j], number[i])
                if number[j] > number[i]:
                    tmp = number[j]
                    number[j] = number[i]
                    number[i] = tmp
            print("================", i, number)
        return number

a=soluTion()
in_num1 = [1, 4, 45, 6, 10, -8]
print("input  : ", in_num1)
rst = a.sortArray(in_num1)
print("output : ", rst)
'''

'''
#####################################################################
# function: LeetCode:Easy 1. Two Sum
# Input: [2, 3, 7, 11, 13], target=9
# Output: [0, 2]

class soluTion(object):
    def findTwoSum(self, number, tgt):
        print(number)
        LenGth = len(number)
        tmpresult = []
        result = []

        for i in range(0, LenGth):
            for j in range(1, LenGth):
                if (number[i] + number[j] == target):
                    tmpresult.append(i)
                    tmpresult.append(j)
                    result.append(tmpresult)
                    tmpresult =[]
        return result

a=soluTion()
#in_num1 = [2, 3, 7, 11, 13]
#target = 9
in_num1 = [1, 4, 45, 6, 10, -8]
target = 16

rst = a.findTwoSum(in_num1, target)
print(rst)
'''


'''
#####################################################################
def appendFile(text, filename):
    with open(filename, "a") as f:
        f.write(text)
        f.write("\n")

infile = "a2"+".out"
appendFile("hahaha", infile)
#####################################################################
'''



'''
#####################################################################
# function: swap array
# Input: [1,2,3,4]
# Output: [4,3,2,1]

class soluTion(object):
    def swaparray(self, number):
        print(number)
        LenGth = len(number)
        for i in range(LenGth/2):
            tmp = number[i]
            number[i] = number[LenGth-1-i]
            number[LenGth-1-i] = tmp
            #print(i, number[i], LenGth-1-i, number[LenGth-1-i])
        return number

a=soluTion()
in_num1 = [1,2,3,4]
rst = a.swaparray(in_num1)
print(rst)
'''

'''
#####################################################################
# function: find second duplicate
# Input:  ['a', 'b', 'c', 'a', 'b', 'd'] -> a

class soluTion(object):
    def find2ndDuplicate(self, inPut):
        if not inPut:
            return "no inPut"
        res = []
        dupres = []
        k = 0
        for i in inPut:
            #print(i)
            if i not in res:
                res.append(i)
            else:
                dupres.append(i)
                #break
        return dupres[1]

#inPutVar = []
inPutVar = ['a', 'b', 'c', 'a', 'b', 'd']
a = soluTion()
print("input  ", inPutVar)
rst = a.find2ndDuplicate(inPutVar)
print("output ", rst)
'''



'''
#####################################################################
# function: find first duplicate
# Input:  ['a', 'b', 'c', 'a', 'b', 'd'] -> a

class soluTion(object):
    def find1stduplicate(self, inPut):
        res = []
        dupres = []
        k = 0
        for i in inPut:
            #print(i)
            if i not in res:
                res.append(i)
            else:
                dupres.append(i)
                break
        return dupres[0]

inPutVar = ['a', 'b', 'c', 'a', 'b', 'd']
a = soluTion()
print("input  ", inPutVar)
rst = a.find1stduplicate(inPutVar)
print("output ", rst)
'''


'''
#####################################################################
# function: delete duplicate in string
# Input:  ("abcabc") -> Output: ('a', 'b', 'c')
# convert tuple to list because string needs to be converted to char
# list = list(tuple), tuple = tuple(list)
# list to dictionary
# 1) res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
# 2) it = iter(lst)
#    res_dct = dict(zip(it, it))

class soluTion(object):
    def deleteduplicate(self, inPut):
        res = []
        for i in inPut:
            if i not in res:
                res.append(i)
        res = tuple(res)
        return res

a=soluTion()
inPutVar = ("abcabc")
print("input  ", inPutVar)
tmp = list(inPutVar)
inPutVar = tmp
rst = a.deleteduplicate(inPutVar)
print("output ", rst)
'''

'''
#####################################################################
# function: delete duplicate
# Input: ['a', 'b', 'c', 'a', 'b', 'c'] -> Output: ['a', 'b', 'c']
# Input: [1, 3, 5, 6, 3, 5] -> Output: [1, 3, 5, 6]

class soluTion(object):
    def deleteduplicate(self, inPut):
        res = []
        for i in inPut:
            if i not in res:
                res.append(i)
        return res

a=soluTion()
inPutVar = ['a', 'b', 'c', 'a', 'b', 'c']
#inPutVar = [1, 3, 5, 6, 3, 5]
print("input  ", inPutVar)
rst = a.deleteduplicate(inPutVar)
print("output ", rst)
#####################################################################
'''

#####################################################################
#####################################################################
#####################################################################
#####################################################################
# after meeting with SM Kang 2/15/2020
#####################################################################
#####################################################################
#####################################################################
#####################################################################


'''
#####################################################################
# function: LeetCode:Easy 26. return number of array after removing Duplicates from Sorted Array
# Input: [1,1,2]
# Output: [1,2]
# Input: [0,0,1,1,1,2,2,3,3,4]
# Output: [0,1,2,3,4]

class soluTion(object):
    def removeduplicate(self, number):
        print(number)
        #delNo =[]
        LenGth = len(number)
        i = 0;
        j = 1
        while (j < LenGth):
            if number[i] == number[j]:
                j += 1
                #delNo.append(number[i])
            else:
                i += 1
                number[i] = number[j]
                j += 1
                #delNo.append(number[i])
        #print(delNo)
        return i + 1

a=soluTion()
in_num1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
rst = a.removeduplicate(in_num1)
print(rst)
'''



'''
#####################################################################
# function: LeetCode:Easy 189. Rotate Array
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]

## for reference, 
with open("rotatearray.csv", "r") as inputf1:
    myVar = inputf1.readlines()
firstLine = myVar[0]
firstLine = myVar[0].rstrip()
firstlineSplit = firstLine.split(',')
a = int(firstlineSplit[0])
b = int(firstlineSplit[1])
secondLine = myVar[1].rstrip()

print("============================================")
class soluTion(object):
    def rotatearray(self, number, target):
        print(number)
        print("shift right %d " % target)
        for k in range(target):
            LenGth = len(number)
            tmp = number[LenGth-1]
            for i in range(LenGth):
                number[LenGth-1-i] = number[LenGth-2-i]
            number[0] = tmp
        return (number)

a=soluTion()
in_num1 = [11,22,33,44,55,66,77]
target = 3
rst = a.rotatearray(in_num1, target)
print(rst)

in_num2 = [-1,-100,3,99]
target = 2
rst = a.rotatearray(in_num2, target)
print(rst)
'''


'''
#####################################################################
# function: LeetCode:Easy 346. Moving Average from Data Stream
# 1 -> 1
# 10-> (1+10)/2
# 3 -> (1+10+3)/3
# 5 -> (1+10+3+5)/3
class   soluTion(object):
    def __init__(self, size):
        self.size = size
        self.array = []
        self.sum = 0

    def next(self, val):
        self.array.append(val)
        arraylen = len(self.array)

        self.sum += val
        if arraylen < self.size:
            avg = self.sum / arraylen
        else:
            avg = self.sum / self.size

        print(self.array, avg)

##### main routine #####
a = soluTion(3)

a.next(5)
a.next(5)
a.next(5)
a.next(5)
a.next(5)
a.next(5)

rw = ['a']
cmdInfo = ['b', 'c', 'd', 'e']
rw.append(cmdInfo)

print(rw)

for argu in cmdInfo:
    print(argu)
#####################################################################
'''

'''
#####################################################################
# function: linux command line execution by using subprocess
import subprocess

cmdInfo = ['ls', '-l']
proc = subprocess.Popen(cmdInfo)
proc.wait()

cmdInfo = ['./nvmestress.exe', '-ioex=fill', '-slba=%d' % 0, '-nlb=%d' % 65536, '-dev=/dev/nvme0n1']
print(cmdInfo)
pro = subprocess.Popen(cmdInfo)
pro.wait()
del pro

#####################################################################
'''


'''
#####################################################################
# function: LeetCode:Easy 509. Fibonacci Number, recursion, recursive calling
def fibonacci(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return(fibonacci(num-1) + fibonacci(num-2))

number = 7
print("fibonacci of number ", number, " is ", fibonacci(number))
#####################################################################
'''


#2020/02/11
'''
#####################################################################
# function: LeetCode:Easy 20. Valid Parentheses
class soluTion(object):
    #1st solution
    def isValid(self, strs):

stRings = ['()', '([', '[()]', '[]']
a=soluTion()
rst=a.isValid(stRings)
print('result:', rst)
#####################################################################
'''


#2020/02/10
'''
#####################################################################
# function: Jon's python coding question - try again...
infile = open('a.csv', "r")
outfile = open('a1.out', "w")

linelength = 1
a_out = {}
pass_cnt = 0
fail_cnt = 0

while(linelength != 0):
    #print('=======================================')
    myVar = infile.readline()
    linelength = len(myVar)
    if (linelength == 0):
        break

    myVar_split = myVar.split(',')

    if not myVar_split[0] in a_out:
        pass_fail = {'pass':0, 'fail':0}
        b = {myVar_split[0]:pass_fail}
        a_out.update(b)

    if (myVar_split[2] == 'pass\n'):
        pass_cnt = 1
    else:
        fail_cnt = 1
    a_out[myVar_split[0]]['pass'] = a_out[myVar_split[0]]['pass'] + pass_cnt
    a_out[myVar_split[0]]['fail'] = a_out[myVar_split[0]]['fail'] + fail_cnt

    pass_cnt = 0
    fail_cnt = 0

#print(a_out)

for i, j in a_out.items():
    #print(i)
    #print(j)
    a=[0,0]
    cnt=0
    for k, m in j.items():
        #print(k)
        #print(m)
        a[cnt] = m
        cnt += 1
    outfile.write(i + ' ' + 'pass=' + str(a[0]) + ' fail=' + str(a[1]) + '\n')
'''

'''
#####################################################################
# function: LeetCode:Easy 20. Valid Parentheses
class soluTion(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            print("KK_001")
            print(c)
            if c in parmap:
                print("KK_002")
                if parmap[c] == pars[len(pars)-1]:
                    print("KK_003")
                    pars.pop()
            else:
                print("KK_004")
                pars.append(c)
        return len(pars) == 1
#######
class soluTion(object):
    #1st solution
    def isValid(self, strs):
        slen = len(strs)

        for i in range(0, slen):
            print(i, strs[i])
#######

stRings = [')(']
a=soluTion()
rst=a.isValid(stRings)
print('result:', rst)
#####################################################################
'''

'''
#####################################################################
# function: test for simple function
stRings = ['abcde', 'abdde', 'abxxxx', 'abcee']
for i, char in enumerate(stRings[0]):
    print(i, char)

for i, j in enumerate(stRings):
    print(i, j)

print(stRings[2][3:])

a_dict = {'a':1, 'b':2, 'c':3}
print(a_dict)
for i, j in a_dict.items():
    print(i, j)
#####################################################################
'''


'''
#####################################################################
# function: LeetCode:Easy 14. Longest Common Prefix

class soluTion(object):
    #1st solution
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        longest_pre = strs[0]
        for i in range(1,len(strs)):
            while(strs[i].find(longest_pre)!=0):
                longest_pre = longest_pre[:-1]
                if len(longest_pre) == 0:
                    return ""
        return longest_pre
    #1st solution

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        print(shortest_str)
        print('=============================', type(shortest_str))
        for i, char in enumerate(shortest_str):
            print(i, char)
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        return shortest_str

stRings = ['abdddd', 'abdde', 'abxxxx', 'abcee']
a=soluTion()
rst=a.longestCommonPrefix(stRings)
print('result:', rst)
#####################################################################
'''


'''
#####################################################################
# function: LeetCode:Easy 13. Roman to Integer

class soluTion(object):
    def romanToint(self, x):
        print(x)
        xlist = list(x)
        xlen = len(x)
        a = []

        for i in range(0, xlen):
            if (xlist[i]=='I'):
                a.append(1)
            elif (xlist[i]=='V'):
                a.append(5)
            elif (xlist[i]=='X'):
                a.append(10)
            elif (xlist[i]=='L'):
                a.append(50)
            elif (xlist[i]=='C'):
                a.append(100)
            elif (xlist[i]=='D'):
                a.append(500)
            elif (xlist[i]=='M'):
                a.append(1000)

        print(a)
        sum = 0
        for j in range(xlen-1):
            print("j=", j, a[j])
            if a[j] >= a[j+1]:
                sum += a[j]
            else:
                sum -= a[j]
        sum += a[-1]
        return sum

inPut = 'XVII'
a=soluTion()
rst=a.romanToint(inPut)
print(rst)
#####################################################################
'''

'''
#####################################################################
# function: LeetCode:Easy 9. Palindrome Number
# Input: 121
# Output: true
#
# Input: -121
# Output: false

class soluTion(object):
    def isPalindrome(self, x):
        xorg = x
        print(x, xorg)
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
            if x == 0:
                break
        raTio = len(arr)
        print(arr, raTio)
        reTurnVal = 0
        for i in range(0, raTio):
            reTurnVal += arr[i] * 10**(raTio - 1 - i)

        if (siGned == 1):
            reTurnVal *= (-1)

        print("result:", xorg, int(reTurnVal))
        if (xorg == int(reTurnVal)):
            return print("Yes, it is Palindrome")
        else:
            return print("No, it is NOT Palindrome")

inPut = 123
a = soluTion()
a.isPalindrome(inPut)

#####################################################################
'''


'''
#####################################################################
# function: LeetCode:Easy 7. Reverse Integer

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
            if x == 0:
                break
        raTio = len(arr)
        print(arr, raTio)
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

'''
#####################################################################
# function: LeetCode:Easy 1. Two Sum

class soluTion(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    return i, j

a_num = [2, 7, 11, 15]
target = 9
a = soluTion()
rst = a.twoSum(a_num, target)
print(rst)
#####################################################################
'''

#2020/02/09
'''
#####################################################################
# function: Jon's python coding question
inputfile1 = open("a.csv", "r")
testresult = open("a1.out", "w")

pass_fail = {'pass':0, 'fail':0}
a_out = {}
pass_cnt = 0
fail_cnt = 0
linelength = 1
testcount = 0

while (linelength != 0):
    myVar1 = inputfile1.readline()
    linelength = len(myVar1)
    if (linelength == 0):
        break
    var_split = myVar1.split(',')

    if not var_split[0] in a_out:
        pass_fail = {'pass': 0, 'fail': 0}
        b = {var_split[0]:pass_fail}
        a_out.update(b)

    if (var_split[2] == 'pass\n'):
        pass_cnt = 1
    else:
        fail_cnt = 1
    a_out[var_split[0]]['pass'] = a_out[var_split[0]]['pass'] + pass_cnt
    a_out[var_split[0]]['fail'] = a_out[var_split[0]]['fail'] + fail_cnt

    pass_cnt = 0
    fail_cnt = 0

for i, j in a_out.items():
    a = [0,0]
    cnt = 0
    for k, m in j.items():
        a[cnt] = m
        cnt += 1
    testresult.write(i + ' ' + 'pass=' + str(a[1]) + ' fail=' + str(a[0]) + '\n')
#####################################################################
'''

'''
#####################################################################
# function: 
a = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps", "aaaa": "cccc"}
for i, j in a.items():
    print("key is: %s" % i)
    print("value is: %s" % j)
    print("###########################")
#####################################################################
'''

'''
#####################################################################
# function: [example for dictionary]
1. add
a={'av':'db', 'a':'b'}
a['aa']=;'cc'
a={'aa':'cc', 'av':'db', 'a':'b'}
2. print
print(a)
3. looping
for i, j in a.items():
    print(i)
    print(j)
4. update
a={'a':'aa'}
b={'b':'bb', 'c':'cc'}
a.update(b)
a={'a':'aa', 'b':'bb', 'c':'cc'}
5. find
myVal1=inputfile.readline()
num_hit=myVal1.find('aaa') => number of hit column
#####################################################################
'''

'''
#####################################################################
# function: dictionary in dictionary
a={}
b={}
b={1:0}     #pass:fail
a={'fio':b} #fio
print(a)

b={0:1}     #pass:fail
a={'gra':b} #fio
print(a)
#####################################################################
'''



################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################


'''
#####################################################################
# function: Jon's python coding question
#a={'tester':'fio', 'file':'a.png', 'result':'pass'}
#b={'tester':'gra', 'file':'b.png', 'result':'fail'}
#c={'tester':'ung', 'file':'c.png', 'result':'fail'}
#d={'tester':'ung', 'file':'q.png', 'result':'pass'}
#e={'tester':'gra', 'file':'q.png', 'result':'pass'}

inputfile1 = open("a.csv", "r")
testresult = open("a1.out", "w")

pass_fail = {'pass':0, 'fail':0}
a_out = {}
pass_cnt = 0
fail_cnt = 0
linelength = 1
testcount = 0
while(linelength != 0):
    myVar1 = inputfile1.readline()
    #firsthit=myVar1.find('c.jpg')       #firsthit means column number when it encounter 'c.jpg'
    #print(myVar1)
    #print(firsthit)
    #testresult.write(myVar1)
    linelength = len(myVar1)
    #print("KK_ linelength=", linelength)
    if (linelength == 0):
        break
    #testcount = testcount + 1
    var_split=myVar1.split(',')
    #print(var_split[2])
    if(var_split[2] == 'pass\n'):
        print("KK_pass")
        pass_cnt = 1
    else:
        print("KK_fail")
        fail_cnt = 1
    a_out = {var_split[0]:pass_fail}
    #print("KK_a_out #1  ", a_out)
    #print("KK_a_out[var_split[0]]['pass']   ", a_out[var_split[0]]['pass'])
    a_out[var_split[0]]['pass'] += pass_cnt
    a_out[var_split[0]]['fail'] += fail_cnt

    a_out={var_split[0]:pass_fail}
    print("KK_a_out #2  ", a_out)
    #a_upd={var_split[0]:var_split[1]:var_split[2]}
    #print(var_split[0])
    pass_cnt = 0
    fail_cnt = 0
    pass_fail = {'pass': 0, 'fail': 0}
    print("================================")

print("test count=%d" % testcount)
print("end of file")
#####################################################################
'''





'''
##########################################################
##########################################################
#2020/0208
##########################################################
##########################################################
# function: ParseArgs()
import argparse
import sys

def ParseArgs():
    """Parse command line options into globals."""
    global physDrive, physDriveDict, physDriveTxt, utilization, nullio, isFile
    global outputDest, offset, cluster, yes, quickie, verify, fastPrecond

    parser = argparse.ArgumentParser()

    parser.add_argument("--drive", "-d", dest="physDrive",
                        help="Device to test (ex: /dev/nvme0n1)", required=True)
    parser.add_argument("--utilization", "-u", dest="utilization",
                        help="Amount of drive to test (in percent), 1...100",
                        default="100", type=int, required=False)

    args = parser.parse_args()

    physDrive = args.physDrive
    utilization = args.utilization
    #print("physDrive", physDrive)

    if (utilization < 1) or (utilization > 100):
        print("ERROR:  Utilization must be between 1...100")
        #parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    ParseArgs()
    print("complete ParseArgs method!\n")
'''
