# Date: 17-Feb-2020
# print spiral of a matrix.
# O(m*n)

class Solution:
    def print_sprial(self, li):        
        start_row = 0
        end_row = len(li) - 1
        start_column = 0
        end_column = len(li[0]) - 1
        while start_column <= end_column and start_row <= end_row:
          # left to right column
          for c in range(start_column, end_column + 1):
            print(li[start_row][c])
          # top to bottom row
          for r in range(start_row + 1, end_row + 1):
            print(li[r][end_column])

          # right to left reverse
          # If there is only row left, that is already covered by left to right
          # traversal
          if start_row < end_row:
            for c in range(end_column - 1, start_column - 1, -1):
              print(li[end_row][c])

          # bottom to top reverse
          # If there is only one column left, that is already covered by top to down
          # traversal
          if start_column < end_column:
            for r in range(end_row - 1, start_row, -1):
              print(li[r][start_column])
          start_row += 1
          end_row -= 1
          start_column += 1
          end_column -= 1

def main():
  s = Solution()
  li = [[1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]]
  s.print_sprial(li)

if __name__ == '__main__':
  main()

# Output:
# -------
# 1
# 2
# 3
# 6
# 9
# 8
# 7
# 4
# 5
