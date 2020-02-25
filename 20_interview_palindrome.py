#! /usr/bin/python2.7
#####################################################################
# https://medium.com/@sarahelson81/top-15-interview-questions-for-test-automation-engineers-e6c20842910
# Question 1
# You are given a word. Now, using your favorite programming language,
# write a code to test if the word hat is given to you is a palindrome.
# [ Palindromes are words that have similar characters from left and right both.
# Ex: noon, radar, civic, etc.]

print("=============================================================")
print("====================== test for interview ===================")
def palendrom(arrayA):
    lenGth = len(arrayA)

    for i in range(lenGth/2):
        tmp = arrayA[i]
        arrayA[i] = arrayA[lenGth-1-i]
        arrayA[lenGth - 1 - i] = tmp
    return arrayA


a = "abcde"
b = list(a)

rst = palendrom(b)
print("rst= ", rst)

result = ""
for i in rst:
    result += i

print("result= ", result)

if result == a:
    print("Palendrom")
else:
    print("Not Palendrom")

