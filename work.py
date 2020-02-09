#!/usr/bin/python3

#2020/02/09
open_a_csv = open("a.csv", "r")
myvar = open_a_csv.readline()
print(myvar)
myvarsplit = myvar.split(',')
print("myvarsplit[0]", myvarsplit[0])
print("myvarsplit[1]", myvarsplit[1])
print("myvarsplit[2]", myvarsplit[2])

# print(lenth(myvarsplit))

'''
#2020/0208
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
