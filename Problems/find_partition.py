# Date: 06-04-2020
# Problem:
# --------
# An arbitrary list of positive integers of any length and in any order
# Determine if the list is partitionable or not. A partitioned list is one
# where it can be split into 2 sub-lists with equal sum. A sub-list can be any
# arbitrary (any set of numbers in any order) selection of numbers out of the
# parent list.
#
# Approach:
# ---------
# - If sum of all elements in list comes out to be odd, then it is not possible
#   to partition list in 2 subsets having same sum
# - We can use DP(bottom up) approach to solve the problem.
#   We can take a 2D array of size (sum/2 + 1)*(n + 1) and
#   fill this array using bottom up approach, see comments in program.
#
# Complexity:
# -----------
# O(n*sum)


def checkEqualSumPossible(arr):
  """
  Returns True if list arr can be divided in 2 subsets having equal sum
  otherwise False.
  """
  if not arr:
    return True

  n = len(arr)
  s = sum(arr)

  # arr can be divided in 2 subsets only if total sum is even otherwise it's
  # not possible to divide array having equal sum.
  if s % 2:
    return False

  # Create a matrix of size - (sum/2 + 1)*(n + 1)
  # dp[i][j] = true if a subset of {arr[0], arr[1], ..arr[j-1]} has sum equal
  # to i, otherwise false
  half_sum = s // 2
  dp = [[None]*(n + 1) for _ in range(half_sum + 1)]

  # Initialize top row as true as sum of 0 is always possible with any subset
  # of numbers - using empty set
  for i in range(n + 1):
    dp[0][i] = True

  # Initialize leftmost column, except part[0][0], as no positive sum is
  # possible with 0 elements
  for i in range(1, half_sum + 1):
    dp[i][0] = False

  # Update matrix using bottom up approach
  for i in range(1, half_sum + 1):
    for j in range(1, n + 1):

      # If sum i is possible with subset of element from arr[0..j-2] then same
      # sum is also possible with subsets of elements from arr[0..j-1].
      dp[i][j] = dp[i][j - 1]

      # In case d[i][j] comes to be false and current element is less than
      # running sum, we can assign value which was at sum = without current
      # element
      if i >= arr[j-1] and (not dp[i][j]):
        dp[i][j] = dp[i - arr[j-1]][j - 1]

  return dp[half_sum][n]

def main():
  arr = [1, 2, 3, 4, 5, 6, 7]
  # arr = [1, 10, 5, 21, 4]
  # arr = [1, 10, 5, 21, 4, 1]
  is_partitionable = checkEqualSumPossible(arr)
  if is_partitionable:
    print('List is partitionable')
  else:
    print('List is not Partitionable')

if __name__ == '__main__':
  main()