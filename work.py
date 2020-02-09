#!/usr/bin/python3

import argparse

def ParseArgs():
    """Parse command line options into globals."""
    global physDrive, physDriveDict, physDriveTxt, utilization, nullio, isFile
    global outputDest, offset, cluster, yes, quickie, verify, fastPrecond

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A tool to easily run FIO to benchmark sustained "
        "performance of NVME\nand other types of SSD.",
        epilog="""
Requirements:\n
* Root access (log in as root, or sudo {prog})
* No filesytems or data on target device
* FIO IO tester (available https://github.com/axboe/fio)
* sdparm to identify the NVME device and serial number
WARNING: All data on the target device will be DESTROYED by this test.""")

    parser.add_argument("--cluster", dest="cluster", action='store_true',
                        help="Run the test on a cluster (--drive in "+
                        "host1:/dev/p1,host2:/dev/ps,...)", required=False)
    parser.add_argument("--verify", dest="verify", action='store_true',
                        help="Have FIO perform data verifications on reads."+
                        " May impact performance", required=False)
    parser.add_argument("--drive", "-d", dest="physDrive",
                        help="Device to test (ex: /dev/nvme0n1)", required=True)
    args = parser.parse_args()

    physDrive = args.physDrive
    print("physDrive", physDrive)



if __name__ == "__main__":
    ParseArgs()
    print("complete!")


'''
print("Hello")
print("update modified code")
'''