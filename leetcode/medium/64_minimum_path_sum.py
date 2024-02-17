"""
https://leetcode.com/problems/minimum-path-sum/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
"""

import math

class Solution:
  def minPathSum(self, grid):
    row = len(grid)
    col = len(grid[0])
    cache = {}
    def path(i, j):
      v1 = math.inf
      v2 = math.inf
      if i == row - 1 and j == col - 1:
        return grid[i][j]
      if (i, j) in cache:
        return cache[(i, j)]
      if i < row - 1:
        v1 = path(i + 1, j)
      if j < col - 1:
        v2 = path(i, j + 1)
      cache[(i, j)] = grid[i][j] + min(v1, v2)
      return cache[(i, j)]
    return path(0, 0)


def main():
  s = Solution()
  print('*********** GRID *****************')
  grid = [[1,3,1],[1,5,1],[4,2,1]]
  print(grid)
  result = s.minPathSum(grid)
  print('*********** MIN PATH SUM ***********')
  print(result)


if __name__ == '__main__':
  main()

# Output:
#---------
# *********** GRID *****************
# [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# *********** MIN PATH SUM ***********
# 7
