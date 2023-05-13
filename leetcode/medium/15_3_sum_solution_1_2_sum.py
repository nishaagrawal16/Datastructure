"""
https://leetcode.com/problems/3sum/

Complexity
----------
O(n^2) time and space O(n)
"""

class Solution:
  def threeSum(self, nums):
    result = set()
    for i, v in enumerate(nums):
      twoSum = -v # 0 - v
      seen = set()
      for vl in nums[i+1:]:
        if twoSum - vl in seen:
          val = sorted([v, vl, twoSum-vl])
          result.add(tuple(val))
        else:
          seen.add(vl)
    return result

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
