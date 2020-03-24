#!/usr/bin/python2.7

class soluTion(object):
    def repeatedstring(self, n, s):
        lenGth = len(s)             # length of 'aba' = 3
        running_count = [0 for ii in range(lenGth)]
        if(s[0] == 'a'):
            running_count[0] = 1
        for ii in range(1, lenGth):
            running_count[ii] = running_count[ii-1]
            if(s[ii] == 'a'):
                running_count[ii] += 1

        k = n/lenGth
        remaining_count = 0
        if(n%lenGth != 0):
            remaining_count = running_count[n%lenGth - 1]
        total_count = k * running_count[lenGth-1] + remaining_count
        return total_count

        '''     #solved by myself but runtine error occurred!!
        lenGth = len(s)
        mok = n/lenGth
        namuji = n%lenGth
        result = ''
        count = 0
        print(mok, namuji)
        for ii in range(mok):
            result = result + s
        for jj in range(namuji):
            result = result + s[jj]
        for kk in range(len(result)):
            if result[kk] == 'a':
                count += 1
        '''
        return count

s = 'aba'
n = 10
s = 'a'
n = 10000000000

a = soluTion()
rst = a.repeatedstring(n, s)
print(rst)