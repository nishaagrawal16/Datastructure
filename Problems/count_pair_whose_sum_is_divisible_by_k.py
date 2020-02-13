# Count pairs in array whose sum is divisible by K
# https://www.geeksforgeeks.org/count-pairs-in-array-whose-sum-is-divisible-by-k/
# O(n)
#      k=4
#   1+3, 2+2
#       k=3
#       1+2

def countKdivPairs(A, n, K):      
    # Create a frequency array to count  
    # occurrences of all remainders when  
    # divided by K 
    freq = [0] * K 
      
    # Count occurrences of all remainders 
    for i in range(n): 
        freq[A[i] % K]+= 1
    print(freq)
    # Find the combination nC2 = n(n-1)/2  
    # If both pairs are divisible by 'K' 
    # oth position contain the count of whose numbers which are completly by k.
    sum = freq[0] * (freq[0] - 1) / 2
      
    # count for all i and (k-i) 
    # freq pairs 
    i = 1
    while i <= K//2 and i != (K - i): 
        sum += freq[i] * freq[K-i] 
        i+= 1
   
    # If K is even: for example pair 2,2
    if K % 2 == 0: 
        sum += (freq[K//2] * (freq[K//2]-1)/2)      
    return int(sum) 
  
# Driver code 
A = [2, 2, 1, 7, 5, 3] 
n = len(A) 
K = 4
print(countKdivPairs(A, n, K))
