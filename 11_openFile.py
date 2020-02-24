#! /usr/bin/python2.7
#'''
#####################################################################
def appendFile(text, filename):
    with open(filename, "a") as f:
        f.write(text)
        f.write("\n")
        f.close()

#infile = "a3"+".out"
#appendFile("hahaha", infile)
appendFile("hahaha", "a3.out")
appendFile("hohoho", "a3.out")


#####################################################################
#'''

outFile = open("a4.out", "w")
outFile.write("HAHAHA\n")
outFile.write("HoHoHo\n")
outFile.close()
