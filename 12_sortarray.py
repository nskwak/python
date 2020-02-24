#! /usr/bin/python2.7
#'''
#####################################################################
# function: sort array
# Input : [1, 4, 45, 6, 10, -8]
# Output: [-8, 1, 4, 6, 10, 45]

def sortArray(arrayIn):
    lenGth = len(arrayIn)
    for i in range(lenGth):
        for j in range(i):
            if(arrayIn[j] > arrayIn[i]):
                tmp = arrayIn[j]
                arrayIn[j] = arrayIn[i]
                arrayIn[i] = tmp
    return arrayIn

a = [1, 4, 45, 6, 10, -8]
print(a)
rst = sortArray(a)
print(rst)
#####################################################################
#'''

print("============================================================")
class soluTion(object):
    def sortArray(self, number):
        LenGth = len(number)
        for i in range(0, LenGth):
            for j in range(0, i):
                #print("j=", j, " i=", i, number[j], number[i])
                if number[j] > number[i]:
                    tmp = number[j]
                    number[j] = number[i]
                    number[i] = tmp
            #print("================", i, number)
        return number

a=soluTion()
in_num1 = [1, 4, 45, 6, 10, -8]
print("input  : ", in_num1)
rst = a.sortArray(in_num1)
print("output : ", rst)
#####################################################################
#'''