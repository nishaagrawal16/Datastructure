"""
https://leetcode.com/problems/search-a-2d-matrix/

Complexity
----------
O(log(m*n)) time and space O(1)
"""

class Solution:
  def searchMatrix(self, matrix, target):
    l = 0
    h = len(matrix) - 1
    while l <= h:
      m = (l + h)//2
      left = 0
      right = len(matrix[m]) - 1
      if target > matrix[m][right]:
        l = m + 1
      elif target < matrix[m][left]:
        h = m - 1
      else:
        return self.findTarget(matrix[m], target)
    return False

  def findTarget(self, matrix, target):
    l = 0
    h = len(matrix) - 1
    while l <= h:
      m = (l+h)//2
      if target == matrix[m]:
        return True
      elif target < matrix[m]:
        h = m - 1
      else:
        l = m + 1
    return False

def main():
  s = Solution()
  print('*********** 2D-MATRIX *****************')
  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
  target = 3
  print(matrix)
  print('Target: ', target)
  result = s.searchMatrix(matrix, target)
  if result:
    print('Element found')
  else:
    print('Element not found')


if __name__ == '__main__':
  main()

# Output:
#---------
# *********** 2D-MATRIX *****************
# [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# Target:  3
# Element found
