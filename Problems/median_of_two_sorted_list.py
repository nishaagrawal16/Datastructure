# Not solved properly
# Need to solve it as O(log(m+n))
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://github.com/hansrajdas/algorithms/blob/master/Level-4/median_in_2_sorted_arrays.py
# ++++++++++++++++

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """ 
    n1 = len(nums1)
    n2 = len(nums2)
    median1 = self.median(nums1)
    median2 = self.median(nums2)
    if not n1 and not n2:
      return median1
    elif not n1:
      return median2
    elif not n2:
      return median1
    print('median1: ', median1, n1)
    print('median2: ', median2, n2)
    if n1 > 2 and n2 > 2:
      if median1 < median2:
        nums1 = [i for i in nums1 if i >= median1]
        nums2 = [j for j in nums2 if j <= median2]
      elif median1 > median2:
        nums1 = [i for i in nums1 if i <= median1]
        nums2 = [j for j in nums2 if j >= median2]
      else:
        return self.findMedianSortedArrays(nums1, nums2)
      print('nums1: ', nums1)
      print('nums2: ', nums2)
      return 9
    elif n1 == 1 and n2 == 1:
      return (float(nums1[0]) + float(nums2[0]))/2
    elif n1 == 2 and n2 == 2:
      return self.median(self.merge_two_list(nums1, nums2))
    elif n1 == 1 and n2 == 2:
      return self.get_middle_item(nums1, nums2)
    elif n1 == 2 and n2 == 1:
      return self.get_middle_item(nums2, nums1)  

  def merge_two_list(self, nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    k = 0
    i = 0
    j = 0
    nums = [0]*4
    while i < n1 and j < n2:
      if nums1[i] <= nums2[j]:
        nums[k] = nums1[i]
        i = i + 1
      else:
        nums[k] = nums2[j]
        j = j + 1
      k = k + 1

    if i < n1:
      nums[k] = nums1[i]
      i = i + 1
      k = k + 1
    if j < n2:
      nums[k] = nums2[j]
      j = j + 1
      k = k + 1
    return nums

  def median(self, nums):
    n = len(nums)
    median = 0.0
    if len(nums) > 2:
      if n%2 == 1: # For Odd
        index = (n - 1)/2
        median = float(nums[index])
      else: # for even
        index = n/2 - 1
        median = (float(nums[index]) + float(nums[index+1]))/2
    elif len(nums) == 2:
      return (float(nums[0]) + float(nums[1]))/2
    elif len(nums) == 1:
      return float(nums[0])
    return median

  def get_middle_item(self, nums1, nums2):
    nums3 = []
    for i in range(len(nums2)):
      if nums1[0] <= nums2[i]:
        nums3.append(nums1[0])
      nums3.append(nums2[i])
      if len(nums3) == 3:
        break
    return float(nums3[1])

def main():
  # nums1 = [10, 15, 20, 25]
  # nums2 = [12, 14, 16, 19]
  nums1 = [1, 1, 1]
  nums2 = [1, 1, 1]
  # nums1 = [1, 3]
  # nums2 = [2]
  # nums1 = [1, 2]
  # nums2 = [1]
  s = Solution()
  median = s.findMedianSortedArrays(nums1, nums2)
  print('median: ', median)

if __name__ == '__main__':
  main()
