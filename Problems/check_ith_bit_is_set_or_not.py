############################################################################
#                               BITWISE OPERATORS
############################################################################
# youtube.com/watch?v=PXlzn60mRKI&list=PLfQN-EvRGF39Vz4UO18BtA1ocnUhGkvk5&index=7
# Lecture 02 - Check a number is even or odd without using modulus(%)
# operator

def evenOdd(n):
    if n & 1 == 1:
        print('%s is odd' % n)
    else:
        print('%s is even' % n)

evenOdd(6)

############################################################################
# Lecture 03 - How many ways you can convert a to b by applying bitwise OR 
# on a | Bit Manipulation
# a = 2 ==> 0 1 0
#           | | |
#           V V V
# b = 3 ==> 0 1 1
#           1*2*1 (times)
# 1|1 = 1
# 1|0 = 1
# 0|1 = 1
# 0|0 = 0

def convertAToB(a, b):
    res = 1
    while a and b:
        if a & 1 == 1:
            if b & 1 == 1:
                res = res*2
            else:
                return 0
        a = a >> 1
        b = b >> 1
    return res
    
print(convertAToB(2, 3))

############################################################################
# Lecture 04 - Find the smallest number greater than ‘n’ with exactly 1 bit
# different in binary form.
# Approach: We need to add 1 in that number and 'OR' with the number. 

def smallestNumber(n):
    return n | (n + 1)
    
print(smallestNumber(13))

############################################################################
# Lecture 05 - Check the ith bit is set or not | Bit Manipulation

def ithBitISSet(n, i):
    if n & (1 << (i-1)):
        print('%s bit is set in number %s' % (i, n))
    else:
        print('%s bit is not set in number %s' %(i, n))

ithBitISSet(11, 3)

############################################################################
# Lecture 06 - Number of bits to represent a number 'n' | Bit Manipulation

def numberOfBits(n):
    i = 0; a = 0
    while a < n:
        a = a + 2**i
        i = i + 1
    return i

print(numberOfBits(10))

############################################################################
# Lecture 07 - Count the set bits in number | Bit Manipulation
# Approach 1:

def countSetBit(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count

# Approach 2:
# a = 2 ==> 0 1 0
#       &   0 0 1
#       ----------
#           0 0 0
# Ans = 1 iteration
#
# b = 3 ==> 0 1 1
#        &  0 1 0
#       -----------
#           0 1 0
#       &   0 0 1
#       ----------
#           0 0 0
# Ans = 2 iteration
# Optimal Solution O(setbits)

def countSetBit(n):
    count = 0
    while n:
        n = n & n-1
        count += 1
    return count
    
print(countSetBit(3))

#############################################################################
# Lecture 08 - Determine a number is power of 2 or not | Bit Manipulation | Leetcode
# 2 ==> 0 0 1 0
# 4 ==> 0 1 0 0
# 8 ==>  1 0 0 0
# Only 1 bit is set for making the power of 2

def powerOfTwo(n):
    if n < 2 :
        print('no')
        return
    if n & n-1 == 0:
        print('yes')
    else:
        print('no')

powerOfTwo(99)

########################################################################


