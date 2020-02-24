#! /usr/bin/python2.7
#'''
#####################################################################
# function: linux command line execution by using subprocess
import subprocess
print("================== ls -l =========================")
cmdInfo = ['ls', '-l']
proc = subprocess.Popen(cmdInfo)
proc.wait()

print("============== nvmestress.exe -ioex=fill ............. ==============")
cmdInfo = ['./nvmestress.exe', '-ioex=fill', '-slba=%d' % 0, '-nlb=%d' % 65536, '-dev=/dev/nvme0n1']
print(cmdInfo)
pro = subprocess.Popen(cmdInfo)
pro.wait()
del pro

#####################################################################
#'''
