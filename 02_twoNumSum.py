#! /usr/bin/python2.7
def sumTwoNunm(arrayN, target):
    lenGth = len(arrayN)

    for i in range(0, lenGth - 1):
        for j in range(1, lenGth - 1):
            if (arrayN[i] + arrayN[j] == target):
                return i, j

a = [1, 2, 3, 5, 7, 8, 9, 10]
target = 9
print(sumTwoNunm(a, target))

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
