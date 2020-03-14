#! /usr/bin/python2.7

print("==============================================")
f = open("83_combined_emailAddr.txt", 'r')
outPut = open("83_combined_emailAddr.out", 'w')

outputList = []
kk = 0
while(True):
    myVar = f.readline()
    if(len(myVar) == 0):
        break
    myVarL = myVar.rstrip('\n')
    myVarList = myVarL.split(' ')
    for i in range(len(myVarList)):
        outputList.append(myVarList[i])
        outPut.write(myVarList[i] + ';')

print(outputList)
print("==============================================")
a = ['1', '2', ' ', '4', '5']
lenGth = len(a)
for i in range(lenGth):
    print("a[%d] = %s" % (i, a[i]))
    if(a[i].isspace() == True):
        print("found space")
print("==============================================")