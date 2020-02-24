#! /usr/bin/python2.7
#'''
#####################################################################
# function: LeetCode:Easy 509. Fibonacci Number, recursion, recursive calling
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
def fibonacci(num):
    if(num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

a = 7
rst = fibonacci(a)
print(rst)
#####################################################################
#'''

'''
#####################################################################
# function: LeetCode:Easy 509. Fibonacci Number, recursion, recursive calling
def fibonacci(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return(fibonacci(num-1) + fibonacci(num-2))

number = 7
print("fibonacci of number ", number, " is ", fibonacci(number))
#####################################################################
'''
