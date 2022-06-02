# Count pairs in array whose sum is divisible by K
# https://www.geeksforgeeks.org/count-pairs-in-array-whose-sum-is-divisible-by-k/
# O(n)
#      k=4
#   1+3, 2+2
#       k=3
#       1+2
# Approach:
# ---------
# 1) Create a frequency array of size k for storing the mod values.
# 2) Count the occurance of the mod value of array value with k => array[i]%K
# 3) nC2 for 0th position pairs which are completly divisible by K
# 4) i*(k-i) pair
# 5) If k is even, count the inplace position pairs [0, 1, 2, 3] here for 2nd position

# Ticky

def countKdivPairs(A, n, K):
    # Create a frequency array to count
    # occurrences of all remainders when
    # divided by K
    freq = [0] * K

    # Count occurrences of all remainders
    for i in range(n):
        freq[A[i] % K]+= 1
    print('freq: ', freq)
    # Find the combination nC2 = n(n-1)/2
    # If both pairs are divisible by 'K'
    # oth position contain the count of whose numbers which are completely divisible by k.
    # For example:
    # ------------
    # Array    = [2, 6, 14, 4, 8, 12, 7, 5, 3] k=4
    # Feq      = [3, 1, 3, 2]
    #             --Fully divisible by 4
    # Total pairs => (4,8), (8, 12), (12, 4) => 3 pairs => 3*2/2 => nC2
    sum = freq[0] * (freq[0] - 1) / 2

    # count for all i and (k-i)
    # freq pairs (pair are from 1st to k-1 elements, 2nd to k-2 and so on)
    i = 1
    while i <= K//2 and i != (K - i):
        sum += freq[i] * freq[K-i]
        i+= 1

    # If K is even for example 4
    # Array    = [2, 6, 14, 4, 8, 12, 7, 5, 3] k=4
    # 2%4 = 2, 6%4 = 2, 14%4 = 2
    # Feq      = [3, 1, 3, 2]
    #                   --
    # For getting 2 pairs, we need to do
    # nC2=> 3C2 => n*(n-1)/2 => 3*(3-1)/2=>3*2/2=>3
    # here pair should be = (2,2) Position 2 will be creating the pairs by own.
    if K % 2 == 0:
        sum += (freq[K//2] * (freq[K//2]-1)/2)
    return int(sum)

# Driver code
# A = [2, 2, 1, 7, 5, 3]
A = [2, 6, 14, 4, 8, 12, 7, 5, 3]
n = len(A)
K = 4
print('Array: ', A)
print('total Pairs: ', countKdivPairs(A, n, K))

# Output:
# -------
# Array:  [2, 2, 1, 7, 5, 3]
# freq:  [0, 2, 2, 2]
# total Pairs:  5

# Array:  [2, 6, 14, 4, 8, 12, 7, 5, 3]
# freq:  [3, 1, 3, 2]
# total Pairs:  8
