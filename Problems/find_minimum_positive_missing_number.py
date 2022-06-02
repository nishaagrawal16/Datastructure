# Find the minimum positive missing number
# Steps:
# ------
# Check 0 < nums < len(arr) and swap that number in their position.
# e.g 3 will be on 2nd position, 4 will be on 3rd position and so on
# Check i+1 != nums[i]
# https://www.youtube.com/watch?v=-lfHWWMmXXM 7:36
# O(n)



class Solutions:
    # A = [3, 4, 7, 1] O(n)
    # Place number 3 at index 3, number 2 at index 2
    # Ignore negative numbers as well as greater than n numbers
    # At last check i index value should be at i index.
    def minimum_missing_number1(self, A):
      i = 0
      n = len(A)
      for i in range(n):
        correctPos = A[i] - 1
        while  1 <= A[i] <= n and A[i] != A[correctPos]:
          A[i], A[correctPos] = A[correctPos], A[i]
          correctPos = A[i] - 1

      for i in range(n):
        if i + 1 != A[i]:
          return i + 1
      return n + 1

    # Create a set, check each i value in nums, if not present return that
    # Time complexity => O(n)
    # Space complexity => O(n)
    def minimum_missing_number2(self, A):
      nums = set(A)
      i = 1
      while i <= len(nums):
        if i not in nums:
          return i
        i += 1
      return i


    # Check 1 is present in the A, if not return 1.
    # Put 1 in place of negative, zero and greater values of n.
    # if x == n place negative at 0th index.
    # Place negative inplace of number's index if number present.
    # Check values greater than 2nd index if we find any positive value,
    # return that index as missing number.
    # Check if 0th index has positive value, return n
    # otherwise return n + 1
    # Time complexity => O(n)
    # Space complexity => O(1)
    def minimum_missing_number3(self, A):
      if 1 not in A:
        return 1
      n = len(A)
      for i in range(n):
        if A[i] <= 0 or A[i] > n:
          A[i] = 1

      for i in range(n):
        x = abs(A[i])
        if x == n:
          A[0] = -abs(A[0])
        else:
          A[x] = -abs(A[x])

      for i in range(2, n):
        if A[i] > 0:
          return i

      if A[0] > 0:
        return n

      return n + 1


def main():
    nums = [3, 4, 7, 1]
    # nums = [5, 7, 2, 1, 8]
    # nums = [3, 4, -1, 0]
    # nums = [1, 2 ,0]
    # nums = [-1, 4, 2, 1, 9, 10]
    # nums = [-10, -3, -100, -1000, -239, 1]
    # nums = [-1, -2]
    # nums = [2, 2, 4, 0, 1, 3, 3, 3, 4, 3]
    # nums = [699, 0, 0, 9, 0, 0, 0, 0, 1]
    # nums = [3,4,-1,1]
    # nums = [99,94,96,11,92,5,91,89,57,85,66,63,84,81,79,61,74,78,77,30,64,13,58,18,70,69,51,12,32,34,9,43,39,8,1,38,49,27,21,45,47,44,53,52,48,19,50,59,3,40,31,82,23,56,37,41,16,28,22,33,65,42,54,20,29,25,10,26,4,60,67,83,62,71,24,35,72,55,75,0,2,46,15,80,6,36,14,73,76,86,88,7,17,87,68,90,95,93,97,98]
    s = Solutions()
    print(s.minimum_missing_number1(nums))
    print(s.minimum_missing_number2(nums))
    print(s.minimum_missing_number3(nums))



if __name__ == '__main__':
    main()

