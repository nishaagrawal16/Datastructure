"""
https://leetcode.com/problems/search-a-2d-matrix/

Complexity
----------
O(row+col) time and space O(1)
"""
class Solution:
  def searchMatrix(self, matrix, target):
    col = len(matrix[0]) - 1
    row = 0
    while row < len(matrix) and col >= 0:
      if matrix[row][col] == target:
        return True
      if matrix[row][col] < target:
        row += 1
      else:
        col -= 1
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
