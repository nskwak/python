#! /usr/bin/python2.7
#'''
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
        print("1: ", self.size)

        self.sum += val
        if arraylen < self.size:
            avg = self.sum / arraylen
        else:
            avg = self.sum / self.size

        print(self.array, avg)

##### main routine #####
a = soluTion(3)

a.next(5)
a.next(15)
a.next(25)
a.next(105)
a.next(105)
a.next(5)

rw = ['a']
cmdInfo = ['b', 'c', 'd', 'e']
rw.append(cmdInfo)

print(rw)

for argu in cmdInfo:
    print(argu)

for argu in rw:
    print(argu)

#####################################################################
#'''
