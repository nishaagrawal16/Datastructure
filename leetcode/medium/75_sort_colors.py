"""
https://leetcode.com/problems/sort-colors/

Complexity
----------
O(n) time and space O(1)
"""

class Solution:
  def sortColors(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
      if nums[mid] == 0:
        nums[mid], nums[low] = nums[low], nums[mid]
        low += 1
        mid += 1
      elif nums[mid] == 1:
        mid += 1
      else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

def main():
  s = Solution()
  print('*********** LIST *****************')
  nums = [2,0,2,1,1,0]
  print(nums)
  s.sortColors(nums)
  print('********** SORT COLORS ***********')
  print(nums)


if __name__ == '__main__':
  main()

# Output:
#---------
# *********** LIST *****************
# [2, 0, 2, 1, 1, 0]
# ********** SORT COLORS ***********
# [0, 0, 1, 1, 2, 2]
