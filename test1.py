#! /usr/bin/python2.7

f = open("a.txt", 'r')
myVar = f.readline()
print(myVar)
_numlist = []
lines = myVar.split('\n')
print(lines)
del _numlist[:]
for line in lines:
    print("1: ", line)
    if line.startswith('crw--'):
        print("2: ", line)
        print("3: ", line.split('nvme')[-1])
        print("4: ", line.split('nvme')[0])
        print("5: ", line.split('nvme')[1])
        num=eval(line.split('nvme')[-1])
        _numlist.append(num)

print("_numlist: ", _numlist)


import subprocess

print("================== ls -l /dev=========================")
cmdInfo = ['ls', '-l', '/dev']
proc = subprocess.Popen(cmdInfo)
proc.wait()

print("============== grep crw, grep nvme ===================")
pipeCliCmds = [['grep', 'crw'], ['grep', 'nvme']]

subPipe = []
for cliCmd in pipeCliCmds:
    subPipe.append(list(cliCmd))

procMain=proc
for sub in subPipe:
    #pro = subprocess.Popen(sub)
    proc = subprocess.Popen(sub, stdin=proc.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #pro.wait()

procMain.stdout()

#####################################################################
