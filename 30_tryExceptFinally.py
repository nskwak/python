#! /usr/bin/python2.7
#####################################################################
# function: try, except, else, finally
# https://www.youtube.com/watch?v=NIWwJbo-9_8&t=198s
#
#
import sys

print("======================================================")
arrA = ['a', 0, 2]

lenGth = len(arrA)

for inP in arrA:
    try:
        print("The entry is", inP)
        r = 1/int(inP)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

print("The reciprocal of", inP,"is",r)

print("======================================================")
f = None
try:
    try:
        f = open("aa.csv")
        text = f.read()
        print(text)
    except IOError:
        print 'An IOError occurred'
finally:
    if f:
        f.close()
print("======================================================")
try:
    f = open("aa.csv")
    var = bad_var
except Exception as e:
    print(e)

print("\n")
print("======================================================")
print("======== try, except, except, else, finally ==========")
print("======================================================")

try:
    print("1. try===================")
    f = open("a.txt")
    var = bad_var                   # no bad_var so goto Exception
    if f.name == 'a.txt':
        raise Exception             # raise Exception but no print(e)
except IOError as e:
    print("2. except IOError =======")
    print(e)
except Exception as e:
    print("3. except Exception =====")
    print(e)
else:
    print("4. else==================")
    print(f.read())
    f.close()
finally:                            # always come to finally
    print("5. finally===============")
    print("Executing Finally...")