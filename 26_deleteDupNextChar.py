#! /usr/bin/python2.7
# function: remove next duplicate in array.
# Input: abbcadaef
# Output: abcadaef

def deletenextdup(arrayN):
    lenGth = len(arrayN)
    loopcnt = 0
    i = 0
    j = 1
    result = []
    while(j < lenGth):
        loopcnt += 1
        if arrayN[i] == arrayN[j]:
            print("if", loopcnt, arrayN[i], arrayN[j])
            result.append(arrayN[i])
            i += 2
            j += 2
        else:
            print("el", loopcnt, arrayN[i], arrayN[j])
            if loopcnt == 1:
                result.append(arrayN[i])
            result.append(arrayN[j])
            i += 1
            j += 1

    print("loopcnt : %d", loopcnt)
    return result

a = "abbcadaef"
a = list(a)
print(a)
rst = deletenextdup(a)
print(rst)
