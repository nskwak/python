#####################################################################
# Jon's python coding question - try again...
infile = open('a.csv', "r")
outfile = open('a1.out', "w")

linelength = 1
a_out = {}
pass_cnt = 0
fail_cnt = 0

while(linelength != 0):
    print('=======================================')
    myVar = infile.readline()
    linelength = len(myVar)
    myVar_split = myVar.split(',')
    print(myVar_split)
    print(myVar_split[0])
    print(myVar_split[1])
    print(myVar_split[2])

    if not myVar_split[0] in a_out:
        pass_fail = {'pass':0, 'fail':0}
        b = {myVar_split[0]:pass_fail}
        a_out.update(b)

    if (myVar_split[2] == 'pass\n'):
        pass_cnt = 1
    else:
        fail_cnt = 1

    #a_out[myVar_split[0]]['pass'] = a_out[myVar_split[0]]['pass'] + pass_cnt
    #a_out[myVar_split[0]]['fail'] = a_out[myVar_split[0]]['fail'] + fail_cnt

    print(a_out)


