"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Complexity
----------
O(logn)
"""

class Solution:
  def search(self, nums, target):
    l = 0
    h = len(nums) - 1
    while l <= h:
      m = (l + h)//2
      if target == nums[m]:
        return m
      if nums[m] < nums[h]:
        if nums[m] < target <= nums[h]:
          l = m + 1
        else:
          h = m - 1
      else:
        if nums[l] <= target < nums[m]:
          h = m - 1
        else:
          l = m + 1

    return -1

def main():
  s = Solution()
  nums = [4,5,6,7,0,1,2]
  target = 0
  print('nums = ', nums)
  print('target = ', target)
  output = s.search(nums, target)
  print('Output : ', output)


if __name__ == '__main__':
  main()

# Output:
#---------
# nums =  [4, 5, 6, 7, 0, 1, 2]
# target =  0
# Output :  4

