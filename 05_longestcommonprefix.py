#! /usr/bin/python2.7
'''
a = ['1', 'b', 'd', '5']
for i in a:
    print(i)
lisT = {'a':1, 'b':2, 'c':3}
for i, j in lisT.items():
    print(i, j)
'''

#'''
#####################################################################
# function: LeetCode:Easy 14. Longest Common Prefix

class soluTion(object):
    #1st solution
    #def longestCommonPrefix(self, strs):
    #    if not strs: return ""
    #    longest_pre = strs[0]
    #    for i in range(1,len(strs)):
    #        while(strs[i].find(longest_pre)!=0):
    #            longest_pre = longest_pre[:-1]
    #            if len(longest_pre) == 0:
    #                return ""
    #    return longest_pre
    #1st solution

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        print("shortest_str: ", shortest_str)
        print('=============================', type(shortest_str))
        for i, char in enumerate(shortest_str):
            print("i, char: ", i, char)
            for other in strs:
                print("i, other[i]: ", i, other[i])
                if other[i] != char:
                    return shortest_str[:i]
        return shortest_str

stRings = ['abdddd', 'abdde', 'abxxxx', 'abcee']
a=soluTion()
rst=a.longestCommonPrefix(stRings)
print('result:', rst)

#####################################################################
# function: test for simple function
print("=====================================")
print("=====================================")
print("=====================================\n")
stRings = ['abcde', 'abdde', 'abxxxx', 'abcee']
for i, char in enumerate(stRings[0]):
    print(i, char)

print("=====================================\n")
for i, j in enumerate(stRings):
    print(i, j)

print("=====================================\n")
print(stRings[2][3:])

print("=====================================\n")
a_dict = {'a':1, 'b':2, 'c':3}
print(a_dict)
for i, j in a_dict.items():
    print(i, j)
#####################################################################


#####################################################################
#'''
