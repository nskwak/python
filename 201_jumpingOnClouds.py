#! /usr/bin/python2.7

####################################################################
# hackerrank.com: Jumping on the Clouds
# input = [0, 1, 0, 0, 0, 1, 0]
# n = 7
# output = 3


class soluTion:
    def jumpingOnClouds(self, c):
        n = len(c)
        counts = []
        counts.append(0)
        if(c[1] == 1):
            counts.append(1000)
        else:
            counts.append(1)
        for i in range(2,n):
            if(c[i]==1):
                counts.append(1000)
            else:
                tmp = 1 + min(counts[i-1], counts[i-2])
                counts.append(tmp)
        return counts[n-1]


arrayN = [0, 1, 0, 0, 0, 1, 0]
a = soluTion()
rst = a.jumpingOnClouds(arrayN)
print(rst)