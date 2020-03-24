#! /usr/bin/python2.7

####################################################################
# hackerrank.com: Sock Merchant
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# input = [1,2,1,2,1,3,2]
# n=7
# output = 2


class soluTion:
    def SockMerchant(self, n, ar):
        ar.sort()
        result, prev = 0, None
        for curr in ar:
            if prev == curr:
                result += 1
                prev = None
            else:
                prev = curr
        return result

        '''
        result = {}
        for i in ar:
            if i not in result:
                tmp = {i:0}
                result.update(tmp)
            result[i] += 1
        pair = 0
        for i, j in result.items():
            pair += (j / 2)
        return pair
        '''

arrayN = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#arrayN = [1,2,1,2,1,3,2]
#arrayN = ['r','b','r','b','r','y','b']
num = len(arrayN)
a = soluTion()
rst = a.SockMerchant(num, arrayN)
print(rst)