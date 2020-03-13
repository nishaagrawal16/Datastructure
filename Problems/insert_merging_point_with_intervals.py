# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
# Example 1:
# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9]
# would result in [1,2],[3,10],[12,16].
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# Make sure the returned intervals are also sorted.
# O(n)
# Your Input: (1 3), (6 9), (10 15)
# 10 5
# Expected output is (1, 3) (5, 15) # x < y
# 
# 6 0
# Expected output is (0, 9) (10, 15) # x < y
# 
# 4 9
# Expected output is (1, 3) (4, 9) (10, 15)
# 
# 2 2
# Expected output is (1, 3) (6, 9) (10, 15)
# 
# -1 0
# Expected output is (-1, 0) (1, 3) (6, 9) (10, 15)
# 
# 5 15
# Expected output is (1, 3) (5, 15)
# 
# -15 15
# Expected output is (-15, 15)
# 
# 9 4
# Expected output is (1, 3) (4, 9) (10, 15) x < y
# 
# 7 7
# Expected output is (1, 3) (6, 9) (10, 15)
# Tricky (Need to find some alternate approach)
# +++++++++++++++++++

class Solutions:
  def overlapping(self, li):
    j = 0
    while j < len(li) - 1:
      if li[j][1] >= li[j+1][0]:
        flag = 1
        new_elem = [li[j][0], li[j+1][1]]
        del li[j]
        del li[j]
        li.insert(j, new_elem)
        # print('li: ', li)
      else:
        j += 1


def main():
  s = Solutions()
  # li = [[1,2],[3,5],[6,7],[8,10],[12,16]]
  # merge_point = [4,9]
  li = [[1,3],[6,9], [10, 15]]
  merge_point = [7, 7]
  n = len(li)
  # Swap the intervals if 1st is greater.
  if merge_point[0] > merge_point[1]:
    merge_point[0], merge_point[1] = merge_point[1], merge_point[0]

  if merge_point[0] <= li[0][0] and merge_point[1] >= li[n-1][1]: # If merging point cover all the intervals. -15 15
    li = [merge_point]  
  elif merge_point[0] <= li[0][0] and merge_point[1] <= li[0][1]: # if given merging point are smaller than 1st. -1 0
    li.insert(0, merge_point)
  elif merge_point[0] >= li[n-1][0] and merge_point[1] >= li[n-1][1]: # if given merging point are greater than last
    li.insert(n, merge_point)
  else:
    # Merging points lies between the intervals
    present_interval = 0
    # If given merging point is already in the interval (2, 2)
    for i in range(n):
      if li[i][0] >= merge_point[0] and li[i][1] >= merge_point[1]:
        if i-1 >= 0 and merge_point[0] >= li[i-1][0] and merge_point[1]<= li[i-1][1]:
          present_interval = 1
          break
    if present_interval == 0:
      # If both merging point are in the middle and
      # in the correct increasing order. (4, 9)
      correct_order = 0
      for i in range(n):
        if li[i][0] >= merge_point[0] and li[i][1] >= merge_point[1]:
          if i-1 >= 0 and merge_point[0] >= li[i-1][0] and merge_point[1] >= li[i-1][1]:
            correct_order = 1
            li.insert(i, merge_point)
            break
      # If both merging point are in the middle but not in
      # correct increasing order. 5, 15
      if correct_order == 0:
        flag_x = 0 # x element is in the end
        for i in range(n):
          if li[i][0] >= merge_point[0]:
            flag_x = 1
            li.insert(i, [merge_point[0], li[i][1]])
            break      
        if flag_x == 0: # Need to merge x value at the end
          li.insert(n, [merge_point[0], li[n-1][1]])
        for i in range(len(li)):
          if li[i][1] >= merge_point[1]:            
            if i > 0:
              li.insert(i, [li[i-1][0], merge_point[1]])
            else:
              li.insert(i, [li[i][0], merge_point[1]])
            break
  s.overlapping(li)
  print('final li: ', li)

if __name__ == '__main__':
  main()

