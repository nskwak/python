#! /usr/bin/python2.7
# function: remove next duplicate in array.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        siGned = 0
        if (x < 0):
            siGned = 1
            x = (-1) * x
        rem = []
        while (x != 0):
            rem.append(x % 10)
            x = x / 10
        print(rem)
        result = 0
        lenGth = len(rem)
        for i in range(lenGth):
            result += rem[i] * (10**(lenGth-1-i))

        if (siGned == 1):
            result = (-1) * result
        return result

inPut = -78123
print("input: ", inPut)
a = Solution()
rst = a.reverse(inPut)
print("output: ", rst)