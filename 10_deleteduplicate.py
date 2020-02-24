#! /usr/bin/python2.7

#'''
#####################################################################
# function: LeetCode:Easy 26. return number of array after removing Duplicates from Sorted Array
# Input: [1,1,2]
# Output: [1,2]       -> 2
# Input: [0,0,1,1,1,2,2,3,3,4]
# Output: [0,1,2,3,4] -> 5
print("===========================================================")
def numofdeleteduplicate(arrayIn):
    lenGth = len(arrayIn)
    i = 0
    j = 1
    while(j < lenGth):
        if(arrayIn[i] == arrayIn[j]):
            j += 1  #1:j=2
        else:
            i += 1  #2:i=1 #3:i=2
            arrayIn[i] = arrayIn[j]
            j += 1  #2:j=3 #3:j=4
    return i+1
a = [0,0,1,1,1,2,2,3,3,4]
a = ['a', 'b', 'c', 'a', 'b', 'c']

rst = numofdeleteduplicate(a)
print(rst)
#####################################################################
#'''

#'''
#####################################################################
# function: LeetCode:Easy 26. return number of array after removing Duplicates from Sorted Array
# Input: [1,1,2]
# Output: [1,2]       -> 2
# Input: [0,0,1,1,1,2,2,3,3,4]
# Output: [0,1,2,3,4] -> 5
print("===========================================================")
def numofdeleteduplicate1(arrayIn):
    lenGth = len(arrayIn)
    result = []

    for i in arrayIn:
        if i not in result:
            result.append(i)
    return len(result)

a = [0,0,1,1,1,2,2,3,3,4]
rst = numofdeleteduplicate1(a)
print(rst)
#####################################################################
#'''

#'''
#####################################################################
# function: LeetCode:Easy 26. return number of array after removing Duplicates from Sorted Array
# Input: [1,1,2]
# Output: [1,2]       -> 2
# Input: [0,0,1,1,1,2,2,3,3,4]
# Output: [0,1,2,3,4] -> 5
print("===========================================================")
def deleteduplicate(arrayIn):
    lenGth = len(arrayIn)
    result = []

    for i in arrayIn:
        if i not in result:
            result.append(i)
    return result

a = ['a', 'b', 'c', 'a', 'b', 'c']
#a = [0,0,1,1,1,2,2,3,3,4]
rst = deleteduplicate(a)
print(rst)
#####################################################################
#'''

#'''
#####################################################################
# function: delete duplicate in string
# Input:  ("abcabc") -> Output: ('a', 'b', 'c')
# convert tuple to list because string needs to be converted to char
# list = list(tuple), tuple = tuple(list)
# list to dictionary
# 1) res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
# 2) it = iter(lst)
#    res_dct = dict(zip(it, it))
print("===========================================================")
class soluTion(object):
    def deleteduplicate2(self, inPut):
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
rst = a.deleteduplicate2(inPutVar)

result=""
for i in rst:
    result+=i

print("output ", result)
#'''


#'''
#####################################################################
# function: find first duplicate
# Input:  ['a', 'b', 'c', 'a', 'b', 'd'] -> a
print("===========================================================")
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
print(rst)
#'''

#'''
#####################################################################
# function: find second duplicate
# Input:  ['a', 'b', 'c', 'a', 'b', 'd'] -> b
print("===========================================================")
def find2ndduplicate(arrayIn):
    res = []
    dupres = []
    for i in arrayIn:
        if i not in res:
            res.append(i)
        else:
            dupres.append(i)
    return dupres[1]

a = ['a', 'b', 'c', 'a', 'b', 'd']
rst = find2ndduplicate(a)
print(rst)


#####################################################################
#'''