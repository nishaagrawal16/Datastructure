"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Complexity
----------
O(logn)
"""
class Solution:
  def findMin(self, nums):
    l = 0
    h = len(nums) - 1
    while l < h:
      m = (l + h)//2
      if nums[m] <= nums[h]:
        h = m
      else: # nums[m] > nums[h]
        l = m + 1
    return nums[l]

def main():
  s = Solution()
  print('*********** LIST *****************')
  nums = [3,4,5,1,2]
  print(nums)
  minVal = s.findMin(nums)
  print('Minimum Value: ', minVal)


if __name__ == '__main__':
  main()

# Output:
#---------
# *********** LIST *****************
# [3, 4, 5, 1, 2]
# Minimum Value:  1
