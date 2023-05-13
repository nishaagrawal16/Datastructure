"""
https://leetcode.com/problems/3sum/

Approach:
Sort the nums list.
Take 1st element as 1st number.
Find out the 0 - first number.
Choose left and right pointers.
find sum of left + right pointer's value
if sum == target add them in the result.
if sum < target: increase left pointer otherwise decrease right pointer.

Complexity
----------
O(n^2) time and space O(n)
"""

class Solution:
  def threeSum(self, nums):
    nums.sort()
    result = set()
    i = 0
    while i < len(nums):
      twoSum = -nums[i] # 0 - nums[i]
      seen = set()
      self.calculateTwoSum(nums[i+1:], twoSum, result)
      i += 1
    return list(result)

  def calculateTwoSum(self, nums, target, result):
    l = 0
    r = len(nums) - 1
    while l < r:
      s = nums[l] + nums[r]
      if s == target:
        val = (-target, nums[l], nums[r])
        result.add(val)
        l += 1
        r -= 1
      elif s < target:
        l += 1
      else:
        r -= 1

def main():
  s = Solution()
  print('*********** LIST *****************')
  nums = [-1,0,1,2,-1,-4]
  print(nums)
  result = s.threeSum(nums)
  print('********** 3 SUM RESULT **********')
  print(result)


if __name__ == '__main__':
  main()

# Output:
#---------
# *********** LIST *****************
# [-1, 0, 1, 2, -1, -4]
# ********** 3 SUM RESULT **********
# {(-1, 0, 1), (-1, -1, 2)}
