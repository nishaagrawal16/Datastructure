# ************************************************
# Sum of two digit is equal to target
# O(n2)
# ***********************************************

class Solution(object):
  # O(n2)
  def sum_of_number(self, nums, target):
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
          return (i, j)

  # O(n)
  def sum_of_numbers_dict(self, nums, target):
    d = dict()
    for i in range(len(nums)):
      num = nums[i]
      rem = target - num
      if rem in d:
        return (d[rem], i)
      else:
        d[num] = i
    return (-1, -1)

def main():  
  s = Solution()
  nums = [2, 5, 6, 3, 4]
  n1, n2 = s.sum_of_number(nums, 10)
  print('Target: ', 10)
  print('numbers are: {} , {}'.format(nums[n1], nums[n2]))
  
  n1, n2 = s.sum_of_numbers_dict(nums, 10)
  print 'Target: ', 10
  if n1 != -1 and n2 != -1:
    print 'numbers are: {} , {}'.format(nums[n1], nums[n2])

if __name__ == '__main__':
  main()