#! /usr/bin/python2.7
#'''
#####################################################################
# function: find how many same character in array.
# input = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'e']

class soluTion(object):
    def searchDuplicate(self, arrayA):
        lenGth = len(arrayA)
        result = []
        rstDict = {}
        for i in range(lenGth):
            if arrayA[i] not in result:
                result.append(arrayA[i])
            else:
                if arrayA[i] not in rstDict:
                    tmp = {arrayA[i]: 2}
                    rstDict.update(tmp)
                else:
                    rstDict[arrayA[i]] += 1
        return result, rstDict

in_arr = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'e']
a = soluTion()
print(in_arr)
rst = a.searchDuplicate(in_arr)
print(rst)

#####################################################################
#'''

#'''
#####################################################################
# function: find how many same character in array.
print("===================================================================")
class soluTion(object):
    def searchDuplicate(self, inputCharArr):
        lenGth = len(inputCharArr)
        res = []
        resdup ={}
        for inp in inputCharArr:
            if inp not in res:
                res.append(inp)
            else:
                if inp not in resdup:
                    tmp = {inp : 1}
                    resdup.update(tmp)
                else:
                    resdup[inp] += 1
        return resdup

in_arr = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'e']
a = soluTion()
print(in_arr)
rst = a.searchDuplicate(in_arr)
print(rst)

#####################################################################
#'''
