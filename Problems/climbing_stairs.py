# Date: 18-Feb-2020
# Need to climb the stairs in different ways
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top? 
# https://leetcode.com/problems/climbing-stairs/solution/
# Example:
#       5
# 1+1+1+1+1, 2+1+1+1, 2+2+1
#            1+2+1+1, 1+2+2
#            1+1+2+1, 2+1+2
#            1+1+1+2,
# total 8 ways

class Solutions:
  # Approach1: Dynamic Programming
  # Time complexity O(n)
  # Space Complexity O(n)
  def climbingStairsUsingDP(self, n):
    if n == 1:
      return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
      dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

  # Approach2: Fibonacci Number
  # Time complexity O(n)
  # Space Complexity O(1)
  def climbingStairsusingFib(self, n):
    if n == 1:
      return 1
    first = 1
    second = 2
    for i in range(3, n+1):
      third = first + second
      first = second
      second = third
    return second

  def climbingStairsusingFibRecur(self, n):
    if n == 1:
      return 1
    if n == 2:
      return 2    
    return self.climbingStairsusingFibRecur(n-1) + self.climbingStairsusingFibRecur(n-2)


def main():
  s = Solutions()
  print(s.climbingStairsUsingDP(5))
  print(s.climbingStairsusingFib(5))
  print(s.climbingStairsusingFibRecur(5))

if __name__ == '__main__':
  main()
