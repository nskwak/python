#! /usr/bin/python2.7

####################################################################
## [input file] ####################################################
## fio,a.png,fail
## fio,c.jpg,pass
## ung,q.jpg,fail
## [output file] ###################################################
## cli pass=1 fail=3
## gra pass=2 fail=2
##

f = open("01_jonRdWrFileAgain.csv", 'r')
oUt = open("01_jonRdWrFileAgain.out", 'w')
result ={}
#passfail = {"pass":0, "fail":0}
lenGthline = 0
while(True):
    MyVar = f.readline()
    lenGthline = len(MyVar)
    if lenGthline == 0:
        break
    MyVar = MyVar.rstrip()
    MyVarDict = MyVar.split(',')
    if MyVarDict[0] not in result:
        passfail = {"pass": 0, "fail": 0}
        tmp = {MyVarDict[0]:passfail}
        result.update(tmp)
    if MyVarDict[2] == 'pass':
        result[MyVarDict[0]]['pass'] += 1
    else:
        result[MyVarDict[0]]['fail'] += 1

for i, j in result.items():
    #print(i, j['pass'], j['fail'])
    ii = j['pass']
    jj = j['fail']
    oUt.write(i + " " + "pass=" + str(ii) + " fail=" + str(jj) + "\n")






    #lenGthline = len(MyVar)        # this does not work
    #if lenGthline == 0:
    #    break