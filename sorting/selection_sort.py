# Date: 20-Jan-2020
# https://www.geeksforgeeks.org/python-program-for-selection-sort/
#
# In selection sort, we need to keep the first position as sorted
# means, we need to take first index as smallest element and compare it
# with the rest of element. If other element has the smallest value than
# first element swap it's value with the smallest one.
# In this way, in the first pass first element will be the smallest.
# On next pass, we need to compare from element 1st till last elements and
# in next pass 2nd to last,...so on
# Example:
# list:  [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
# Pass1: [1, 5, 6, 9, 8, 4, 10, 3, 2, 7]
# Sorted----
# Pass2: [1, 2, 6, 9, 8, 4, 10, 3, 5, 7]
# Sorted -----
# .... So on
# O(n2)

def selection_sort(un_list):
  n = len(un_list)
  for i in range(n):
    smallest_pos = i
    for j in range(i+1, n):
      if un_list[smallest_pos] > un_list[j]:
        smallest_pos = j
    if smallest_pos:
      temp = un_list[i]
      un_list[i] = un_list[smallest_pos]
      un_list[smallest_pos] = temp

def main():
  unsorted_list = [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
  print('************ UNSORTED LIST **************')
  print(unsorted_list)
  selection_sort(unsorted_list)
  print('************** SORTED LIST **************')
  print(unsorted_list)


if __name__ == '__main__':
  main()

# Output:
# -------
# ************ UNSORTED LIST **************
# [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
# ************** SORTED LIST **************
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
