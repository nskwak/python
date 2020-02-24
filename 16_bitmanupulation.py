#! /usr/bin/python2.7

#'''
#####################################################################
# function: bit maipulation
# Cracking code page 58, 5.6
# problem 2) b0 and b1 swapped, b2 and b3 are swapped
#####################################################################

def swapbit(x):
    return (((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1))

e = 0x11111111
print(swapbit(e), hex(swapbit(e)))
#####################################################################
#'''


#'''
#####################################################################
# function: bit maipulation
# Cracking code page 58, 5.5
# input: 31(0b11111), 14(0b1110 -> output: 2
#####################################################################

a = 31
b = 14
c = a^b
count = 0
while True:
    print(c, bin(c))
    if (c & 1) == 1:
        count += 1
    c = c >> 1
    if (c == 0):
        break

print(count)
#####################################################################
#'''

#'''
#####################################################################
# function: bit maipulation
# Cracking code page 58, 5.5
# input: 31, 14 -> output: 2
#####################################################################

def countXorValue(in_num):
    count = 0
    while(in_num):
        count += in_num & 1
        in_num >>= 1
    return count
a = 31
b = 14

print(countXorValue(a^b))
#####################################################################
#'''

#'''
#####################################################################
# function: bit maipulation
# Cracking code page 57, 5.1
# a)  N = 1024 (10000000000),
#     M = 19 (10011),
#     i = 2, j = 6
#     Output : 1100 (10001001100)
# b)  N = 1201 (10010110001)
#     M = 8 (1000)
#     i = 3, j = 6
#     Output: 1217 (10011000001)
#####################################################################
print("======================================================================")
N = 0b10010110001       #1201
M = 0b1000              #8
i = 3
j = 6

captured_bit = (1<<i) -1
cleared_bit = -1 << (j+1)
print(N, bin(N))
print("captured_bit: ", bin(captured_bit))
print("cleared_bit: ", bin(cleared_bit))

a = N & cleared_bit     #
print(a, bin(a))

b = M << i
c = N & captured_bit
d = a | b | c

print(d, bin(d))
#'''


#'''
#####################################################################
# function: bit maipulation
# Cracking code page 57, 5.1
# a)  N = 1024 (10000000000),
#     M = 19 (10011),
#     i = 2, j = 6
#     Output : 1100 (10001001100)
# b)  N = 1201 (10010110001)
#     M = 8 (1000)
#     i = 3, j = 6
#     Output: 1217 (10011000001)
#####################################################################
print("======================================================================")
N = 0b10010110001       #1201
M = 0b1000              #8
i = 3
j = 6

print("1. N = ", N, bin(N))
capture_mask = (1 << i) - 1         #i = 3 -> capture_mask = 7 = 0b111
captured_bit = N & capture_mask     #captured_bit = 001
print("2. N = ", captured_bit, bin(captured_bit))

clear_mask = -1 << (j+1)            #j = 6 -> clear_mask =
cleared_bit = N & clear_mask        # N & 0000000
print("3. N = ", cleared_bit, bin(cleared_bit))

M <<= i
cleared_bit |= M
print("4. N | (M<<i) ", cleared_bit, bin(cleared_bit))

result = cleared_bit | captured_bit
print("5. N | captured_bit(& 111) ", result, bin(result))
#####################################################################
#'''
