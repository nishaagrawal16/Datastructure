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
# binary: floor(log2(n) + 1)
# decimal: floor(log10(n) + 1)

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
# Lecture 09 - Determine a number is power of 4 or not | Bit Manipulation | Leetcode

import math
def powerOfFour(n):
    count = 0
    if n < 4 :
        return False
    # It means number is of power of 2.
    if n & n-1 == 0:
        # find number of bits in binary.
        i = math.floor(math.log2(n) + 1)
        # Checks 1's bit is on which location(odd for power of 4)    
        if i%2 != 0:
            return True
    return False

print(powerOfFour(16))

##########################################################################
# Lecture 10 - XOR Properties | Bit Manipulation

# XOR properties:
#     1^0 = 1
#     0^1 = 1
#     1^1 = 0
#     0^0 = 0
    
#  1. A^0 = A
#  2. A^A = 0
#  3. A^B = B^A
#  4. A+B = A^B + 2*(A&B)

########################################################################
# Lecture 11 - XORSN (codechef) | Bit Manipulation
# Find XOR[1, n]: 1^2^3^4^5^...n

def XORTillN(n):
    rem = n % 4
    if rem == 0:
        return n
    elif rem == 1:
        return 1
    elif rem == 2:
        return n+1
    elif rem == 3:
        return 0

print(XORTillN(5))

##########################################################################
# Lecture 12 - Lonely Integer (Hackerrank) | Bit Manipulation

def findTheUniqueNumber(arr):
    i = 0
    output = 0
    while i < len(arr):
        output = output^arr[i]
        i += 1
    return output

print(findTheUniqueNumber([1, 2, 3, 4, 3, 2, 1]))

########################################################################
# Lecture 13 - Missing Number | Interview Question | Bit Manipulation
# Find the missing number not in the series of N.

def missingNumber(arr, n):
    i = 1
    output = 0
    while i <= n:
        output = output^i
        i += 1
    i = 0
    while i < len(arr):
        output = output^arr[i]
        i += 1
    return output

print(missingNumber([1, 2, 3, 5], 5))

########################################################################
# Lecture 14 - Determining Numbers (Hackerearth) | Bit Manipulation | Amazon Interview Question
# Find the two unique elements in the array.

import math
def twoUniqueNumbers(arr):
    i = 0
    output = 0
    # XOR of all the numbers, so that we can get the sum of unique numbers.
    while i < len(arr):
        output = output^arr[i]
        i += 1
    # In how many bits number can represent.
    bit = math.floor(math.log2(output) + 1)
    unique1 = 0
    unique2 = 0
    i = 0
    while i < len(arr):
        # Check the bit position is set on which number of array,
        # if element set XOR the elements seprately.
        if arr[i] & (1 << (bit-1)):
            unique1 ^= arr[i]
        else:
            unique2 ^= arr[i]
        i += 1
    
    if unique1 < unique2:
        return unique1, unique2
    else:
        return unique2, unique1

print(twoUniqueNumbers([1, 5, 1, 2, 5, 3]))

###########################################################################
# Lecture 15 - Flip the all bits of a Positive Number | Bit Manipulation
# XOR will give the following result.
# 1 -> 0
# 0 -> 1
# If with XOR the given number with 1111(all position should be set)

import math
def flipAllBits(n):
    # In how many bits number can represent.
    bit = math.floor(math.log2(n) + 1)
    a = 1 << (bit - 1) # 1000
    b = a - 1          # 0111
    c = a | b          # 1111
    return n ^ c

# 10 ==> 1010
#  5 ==> 0101
print(flipAllBits(10)) 

##########################################################################
# Lecture 16 - Print all the subsets of an array | Bit Manipulation
# Tutorial
# [1, 2, 3]
#  1  0  0 --> 4
#  0  1  0 --> 2
#  1  1  0 --> 6
#  0  0  1 --> 1
#  1  0  1 --> 5
#  0  1  1 --> 3
#  1  1  1 --> 7
# total = 2**n - 1

def subsetsOfArray(n, arr):
    total = 2**n - 1
    # This is for each binary number.
    for k in range(1, total + 1):
        i = 0
        # This is for each element of array is set or not. 
        for i in range(n):
            if k & (1 << i):
                print(arr[i], end=' '),
        print('')

subsetsOfArray(3, [1, 2, 3])

# Output:
# ------
# 1 
# 2 
# 1 2 
# 3 
# 1 3 
# 2 3 
# 1 2 3 

##########################################################################
# Lecture 17 - Paying Up ( codechef ) | Bit Manipulation Tutorial
# You have n notes and mobster demand for some moneny, if your notes subset
# is equal to the money than you can give him money otherwise no need to
# pay off.

def payingUp(n, arr, money):
    total = 2**n -1
    # This is for each binary number. 
    for k in range(1, total + 1):
        i = 0
        # This is for each element of array is set or not. 
        sum = 0
        for i in range(n):
            if k & (1 << i):
                print(arr[i], end=' '),
                sum += arr[i]
        print('sum: ', sum)
        if sum == money:
            return 'Yes'
    return 'No'

print(payingUp(3, [1, 2, 3], 3))

##########################################################################
# Lecture 18 - Print all subsets of an array of k length | Bit Manipulation
# Tutorial

# Approach-1:
# -----------
def subsetOfKLength(n, arr, lengthOfSubset):
    total = 2**n -1
    # This is for each binary number. 
    for k in range(1, total + 1):
        i = 0
        count = 0
        subset = []
        # This is for each element of array is set or not. 
        for i in range(n):
            if k & (1 << i):
                count += 1
                subset.append(arr[i])
        if count == lengthOfSubset:
            print(subset)
    
subsetOfKLength(4, [1, 2, 3, 4], 2)

# Approach-2:
# -----------
def subsetOfKLength(n, arr, lengthOfSubset):
    total = 2**n -1
    # This is for each binary number. 
    for k in range(1, total + 1):
        i = 0
        k1 = k
        count = 0
        # Check the total set bit.
        while k1:
            k1 = k1 & (k1 - 1)
            count += 1
        if count == lengthOfSubset:
            # This is for each element of array is set or not. 
            for i in range(n):
                if k & (1 << i):
                    print(arr[i], end=' ')
            print('')

subsetOfKLength(4, [1, 2, 3, 4], 2)

# Output:
# ------
# 1 2 
# 1 3 
# 2 3 
# 1 4 
# 2 4 
# 3 4

##########################################################################
# Lecture 19 - Sum vs XOR ( Hackerrank ) | Bit Manipulation Tutorial
# a+b = a^b + 2(a&b)
# for making a+b = a^b, we need to make a&b = 0
# 0 & 1 = 0
# 0 & 0 = 0
# 1 & 0 = 0
# 1 & 1 = 1
# for making it 0 we have two things 0 --> 0(2 ways) and 1 --> 0(1 ways)
# n = 4: 1 0 0
#      & 0 0/1 0/1
#      -----------
#        1* 2* 2 = 4 answer (2**totalUnsetBit)
            
import math
def sumVsXOR(n):
    totalBitRepresent = math.floor(math.log2(n) + 1)
    totalSetBit = 0
    # Check the total set bit.
    while n:
        n = n & (n - 1)
        totalSetBit += 1
    totalUnsetBit = totalBitRepresent - totalSetBit
    return 2**totalUnsetBit # 1 << totalUnsetBit

print(sumVsXOR(4))

