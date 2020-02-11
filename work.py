#!/usr/bin/python3
'''
#####################################################################
# LeetCode:Easy 20. Valid Parentheses
class soluTion(object):
    #1st solution
    def isValid(self, strs):

stRings = ['()', '([', '[()]', '[]']
a=soluTion()
rst=a.isValid(stRings)
print('result:', rst)
#####################################################################
'''


#2020/02/11
#'''
#####################################################################
# LeetCode:Easy 20. Valid Parentheses
class soluTion(object):
    #1st solution
    def isValid(self, strs):

stRings = ['()', '([', '[()]', '[]']
a=soluTion()
rst=a.isValid(stRings)
print('result:', rst)
#####################################################################
#'''


#2020/02/10
'''
#####################################################################
# Jon's python coding question - try again...
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
# LeetCode:Easy 20. Valid Parentheses
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
# test for simple function
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
# LeetCode:Easy 14. Longest Common Prefix

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
# LeetCode:Easy 13. Roman to Integer

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
# LeetCode:Easy 9. Palindrome Number

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
# LeetCode:Easy 7. Reverse Integer

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
# LeetCode:Easy 1. Two Sum

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
# Jon's python coding question
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
a = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps", "aaaa": "cccc"}
for i, j in a.items():
    print("key is: %s" % i)
    print("value is: %s" % j)
    print("###########################")
#####################################################################
'''

'''
#####################################################################
[example for dictionary]
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
# dictionary in dictionary
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
# Jon's python coding question
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
#####################################################
    while (lineLength != 0):

#    for pp in range(0,4000000):

        myVar1 = j.readline()
        lineLength = len(myVar1)
        if (lineLength == 0):
                        break
#####################################################################
'''





'''
##########################################################
##########################################################
#2020/0208
##########################################################
##########################################################
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
