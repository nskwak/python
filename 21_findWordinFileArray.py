#! /usr/bin/python2.7
#####################################################################
# https://medium.com/@sarahelson81/top-15-interview-questions-for-test-automation-engineers-e6c20842910
# Question 2
# Write a program that returns the count of each word in the file.
print("====================== Question 2 ===========================")
inFile = open("a.csv", "r")
#lineLength = 1
result = {}
while True: #(lineLength != 0):
    inVar = inFile.readline()           # read line
    if(len(inVar) == 0):
        break
    inVarlist = inVar.split(',')        # split by ','
    inVarlist[len(inVarlist)-1] = inVarlist[len(inVarlist)-1].rstrip()  # remove last "\n"
    for i in range(0, len(inVarlist)):
        if inVarlist[i] not in result:  # if inVarDict[i] is not in result dictionary, add
            tmp = {inVarlist[i]: 1}
            result.update(tmp)
        else:
            result[inVarlist[i]] += 1

print("final result = ", result)

# Question 4
# Find out the occurrence of a given word in a given array.
# The word may occur left to right, up to down and vice versa.
print("====================== Question 4 ===========================")
a = [['fda', 'fd', 'gdg', 'fda', 'abc', 'abc'], ['fda', 'fd', 'gdg', 'fda', 'abc', 'abc']]
lenGthRow = len(a)
lenGthCol = len(a[0])

print(lenGthRow, lenGthCol)
result = {}
for i in range(lenGthRow):
    for j in range(lenGthCol):
        if a[i][j] not in result:
            tmp = {a[i][j] : 1}
            result.update(tmp)
        else:
            result[a[i][j]] += 1

print(result)