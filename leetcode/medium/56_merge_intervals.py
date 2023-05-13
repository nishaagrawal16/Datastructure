"""
https://leetcode.com/problems/merge-intervals/

Complexity
----------
O(nlogn) time (Sorting) and space O(n)
"""

class Solution:
  def merge(self, intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    result.append(intervals[0])
    i = 0
    for item in intervals[1:]:
      if item[0] <= result[i][1]:
        result[i][1] = max(item[1], result[i][1])
      else:
        result.append(item)
        i += 1
    return result

def main():
  s = Solution()
  print('*********** INTERVALS *****************')
  intervals = [[1,3],[2,6],[8,10],[15,18]]
  print(intervals)
  result = s.merge(intervals)
  print('*********** MERGE INTERVALS ***********')
  print(result)


if __name__ == '__main__':
  main()

# Output:
#---------
# *********** INTERVALS *****************
# [[1, 3], [2, 6], [8, 10], [15, 18]]
# *********** MERGE INTERVALS ************
# [[1, 6], [8, 10], [15, 18]]
