#!/usr/bin/python3

#2020/02/09
#####################################################################
# Jon's python coding question
inputfile1 = open("a.csv", "r")
testresult = open("a1.out", "w")

pass_fail = {'pass':0, 'fail':0}
a_out = {}
pass_cnt = 0
fail_cnt = 0
linelength = 1
testcount = 0
loopcnt = 1
print('LOOPCNT = ', loopcnt)

'''
while(linelength != 0):
    myVar1 = inputfile1.readline()
    linelength = len(myVar1)
    if (linelength == 0):
        break
    var_split=myVar1.split(',')
    a_out = {var_split[0]:pass_fail}
    print(a_out)
    print("****************************")
'''
while (linelength != 0):
    myVar1 = inputfile1.readline()
    linelength = len(myVar1)
    print("KK_a_out #1  ", a_out)
    if (linelength == 0):
        break
    var_split = myVar1.split(',')

    if var_split[0] in a_out:
        print("exist key", var_split[0])
    else:
        print("new key", var_split[0])
        pass_fail = {'pass': 0, 'fail': 0}
        b = {var_split[0]:pass_fail}
        a_out.update(b)
        #print(a_out)

    if (var_split[2] == 'pass\n'):
        print("pass = ", var_split[0])
        pass_cnt = 1
    else:
        print("fail = ", var_split[0])
        fail_cnt = 1
    print(pass_cnt, fail_cnt)
    a_out[var_split[0]]['pass'] = a_out[var_split[0]]['pass'] + pass_cnt
    a_out[var_split[0]]['fail'] = a_out[var_split[0]]['fail'] + fail_cnt

    #a_out = {var_split[0]: pass_fail}
    #a_out[var_split[0]] = pass_fail
    print("KK_a_out #2  ", a_out)
    pass_cnt = 0
    fail_cnt = 0
    # pass_fail = {'pass': 0, 'fail': 0}
    print("================================")
    loopcnt = loopcnt + 1
    print('LOOPCNT = ', loopcnt)

print("*****************************************************")
print("*****************************************************")
print("final a_out", a_out)
print("*****************************************************")
print("*****************************************************")
#####################################################################
for i, j in a_out.items():
    print("key is ", i)
    print("items is ", j)
    a = [0,0]
    cnt = 0
    for k, m in j.items():
        print('k=', k)
        print('m=', m)
        a[cnt] = m
        cnt += 1
    testresult.write(i + ' ' + 'pass=' + str(a[1]) + ' fail=' + str(a[0]) + '\n')


'''
#####################################################################
a = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps", "aaaa": "cccc"}
for i, j in a.items():
    print("key is: %s" % i)
    print("value is: %s" % j)
    print("###########################")
#####################################################################
'''

'''
#####################################################################
[example for dictionary]
1. add
a={'av':'db', 'a':'b'}
a['aa']=;'cc'
a={'aa':'cc', 'av':'db', 'a':'b'}
2. print
print(a)
3. looping
for i, j in a.items():
    print(i)
    print(j)
4. update
a={'a':'aa'}
b={'b':'bb', 'c':'cc'}
a.update(b)
a={'a':'aa', 'b':'bb', 'c':'cc'}
5. find
myVal1=inputfile.readline()
num_hit=myVal1.find('aaa') => number of hit column
#####################################################################
'''

'''
#####################################################################
# dictionary in dictionary
a={}
b={}
b={1:0}     #pass:fail
a={'fio':b} #fio
print(a)

b={0:1}     #pass:fail
a={'gra':b} #fio
print(a)
#####################################################################
'''


'''
#####################################################################
# Jon's python coding question
#a={'tester':'fio', 'file':'a.png', 'result':'pass'}
#b={'tester':'gra', 'file':'b.png', 'result':'fail'}
#c={'tester':'ung', 'file':'c.png', 'result':'fail'}
#d={'tester':'ung', 'file':'q.png', 'result':'pass'}
#e={'tester':'gra', 'file':'q.png', 'result':'pass'}

inputfile1 = open("a.csv", "r")
testresult = open("a1.out", "w")

pass_fail = {'pass':0, 'fail':0}
a_out = {}
pass_cnt = 0
fail_cnt = 0
linelength = 1
testcount = 0
while(linelength != 0):
    myVar1 = inputfile1.readline()
    #firsthit=myVar1.find('c.jpg')       #firsthit means column number when it encounter 'c.jpg'
    #print(myVar1)
    #print(firsthit)
    #testresult.write(myVar1)
    linelength = len(myVar1)
    #print("KK_ linelength=", linelength)
    if (linelength == 0):
        break
    #testcount = testcount + 1
    var_split=myVar1.split(',')
    #print(var_split[2])
    if(var_split[2] == 'pass\n'):
        print("KK_pass")
        pass_cnt = 1
    else:
        print("KK_fail")
        fail_cnt = 1
    a_out = {var_split[0]:pass_fail}
    #print("KK_a_out #1  ", a_out)
    #print("KK_a_out[var_split[0]]['pass']   ", a_out[var_split[0]]['pass'])
    a_out[var_split[0]]['pass'] += pass_cnt
    a_out[var_split[0]]['fail'] += fail_cnt

    a_out={var_split[0]:pass_fail}
    print("KK_a_out #2  ", a_out)
    #a_upd={var_split[0]:var_split[1]:var_split[2]}
    #print(var_split[0])
    pass_cnt = 0
    fail_cnt = 0
    pass_fail = {'pass': 0, 'fail': 0}
    print("================================")

print("test count=%d" % testcount)
print("end of file")
#####################################################################
'''


'''
#####################################################
    while (lineLength != 0):

#    for pp in range(0,4000000):

        myVar1 = j.readline()
        lineLength = len(myVar1)
        if (lineLength == 0):
                        break
#####################################################################
'''





'''
##########################################################
##########################################################
#2020/0208
##########################################################
##########################################################
import argparse
import sys

def ParseArgs():
    """Parse command line options into globals."""
    global physDrive, physDriveDict, physDriveTxt, utilization, nullio, isFile
    global outputDest, offset, cluster, yes, quickie, verify, fastPrecond

    parser = argparse.ArgumentParser()

    parser.add_argument("--drive", "-d", dest="physDrive",
                        help="Device to test (ex: /dev/nvme0n1)", required=True)
    parser.add_argument("--utilization", "-u", dest="utilization",
                        help="Amount of drive to test (in percent), 1...100",
                        default="100", type=int, required=False)

    args = parser.parse_args()

    physDrive = args.physDrive
    utilization = args.utilization
    #print("physDrive", physDrive)

    if (utilization < 1) or (utilization > 100):
        print("ERROR:  Utilization must be between 1...100")
        #parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    ParseArgs()
    print("complete ParseArgs method!\n")
'''
