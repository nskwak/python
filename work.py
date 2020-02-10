#!/usr/bin/python3

#2020/02/09
'''
#####################################################################
a = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps", "aaaa": "cccc"}
for i, j in a.items():
    print("key is: %s" % i)
    print("value is: %s" % j)
    print("###########################")
#####################################################################
'''

aa = [        ['Team', 'Games'],        ['Arsenal', '38'],        ['Liverpool', '38']    ]

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


#####################################################################
# Jon's python coding question
a={'tester':'fio', 'file':'a.png', 'result':'pass'}
b={'tester':'gra', 'file':'b.png', 'result':'fail'}
c={'tester':'ung', 'file':'c.png', 'result':'fail'}
d={'tester':'ung', 'file':'q.png', 'result':'pass'}
e={'tester':'gra', 'file':'q.png', 'result':'pass'}

inputfile1 = open("a.csv", "r")
testresult = open("a1.out", "w")

a_out ={}
linelength = 1
testcount = 0
while(linelength != 0):
    myVar1 = inputfile1.readline()
    firsthit=myVar1.find('c.jpg')
    print(myVar1)
    print(firsthit)
    testresult.write(myVar1)
    linelength = len(myVar1)
    #print("KK_ linelength=", linelength)
    if (linelength == 0):
        break
    testcount = testcount + 1
    var_split=myVar1.split(',')

    #a_upd={var_split[0]:var_split[1]:var_split[2]}
    #print(var_split[0])

print("test count=%d" % testcount)
print("end of file")
#####################################################################



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
