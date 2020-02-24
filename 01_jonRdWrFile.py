#! /usr/bin/python2.7

#2020/02/23 - re-program

inFile  = open("a.csv", 'r')
outFile = open("a2.out", 'w')

linelength = 1
a_out = {}
pass_cnt = 0
fail_cnt = 0

while(linelength != 0):
    inVar1 = inFile.readline()
    linelength = len(inVar1)
    if(linelength == 0):
        break
    inVar1Dict = inVar1.split(',')

    if not inVar1Dict[0] in a_out:
        passFail = {'pass':0, 'fail':0}
        rst = {inVar1Dict[0]:passFail}
        a_out.update(rst)

    if(inVar1Dict[2].rstrip() == 'pass'):
        a_out[inVar1Dict[0]]['pass'] += 1
    else:
        a_out[inVar1Dict[0]]['fail'] += 1

for i, j in a_out.items():
    a = [0, 0]
    cnt = 0
    for k, l in j.items():
        #print(l)
        a[cnt] = l
        cnt += 1
    outFile.write(i + ' pass=' + str(a[1]) + ' fail=' + str(a[0]) + '\n')

#####################################################################
#####################################################################
# old code
#####################################################################
#####################################################################

#2020/02/09
'''
#####################################################################
# function: Jon's python coding question
inputfile1 = open("a.csv", "r")
testresult = open("a1.out", "w")

pass_fail = {'pass':0, 'fail':0}
a_out = {}
pass_cnt = 0
fail_cnt = 0
linelength = 1
testcount = 0

while (linelength != 0):
    myVar1 = inputfile1.readline()
    linelength = len(myVar1)
    if (linelength == 0):
        break
    var_split = myVar1.split(',')

    if not var_split[0] in a_out:
        pass_fail = {'pass': 0, 'fail': 0}
        b = {var_split[0]:pass_fail}
        a_out.update(b)

    if (var_split[2] == 'pass\n'):
        pass_cnt = 1
    else:
        fail_cnt = 1
    a_out[var_split[0]]['pass'] = a_out[var_split[0]]['pass'] + pass_cnt
    a_out[var_split[0]]['fail'] = a_out[var_split[0]]['fail'] + fail_cnt

    pass_cnt = 0
    fail_cnt = 0

for i, j in a_out.items():
    a = [0,0]
    cnt = 0
    for k, m in j.items():
        a[cnt] = m
        cnt += 1
    testresult.write(i + ' ' + 'pass=' + str(a[1]) + ' fail=' + str(a[0]) + '\n')
#####################################################################
'''
