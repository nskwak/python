#! /usr/bin/python2.7

def ChangeHex(n):
    if (n < 0):
        print(0)
    elif (n<=1):
        print(n)
    else:
        x =(n%16)
        if (x < 10):
            print(x),
        if (x == 10):
            print("A"),
        if (x == 11):
            print("B"),
        if (x == 12):
            print("C"),
        if (x == 13):
            print("D"),
        if (x == 14):
            print("E"),
        if (x == 15):
            print ("F"),
        ChangeHex( n / 16 )

rst = ChangeHex(3743420416)
list(rst)

