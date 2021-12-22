# Date: 20-Jan-2020
# https://www.geeksforgeeks.org/python-program-for-merge-sort/

# Merge Sort is a Divide and Conquer algorithm.
# It divides input array in two halves, calls itself for the two halves and
# then merges the two sorted halves. The merge() function is used for merging two halves.
# Time complexity: O(nlogn)
# Space Complexity: O(n)

def merge(un_list, l, m, r):
  n1 = m - l + 1
  n2 = r - m

  # creats the temporary lists.
  L = [0]*n1
  R = [0]*n2

  # Copy data to temp arrays L[] and R[]
  for i in range(n1):
    L[i] = un_list[l + i]
  for j in range(n2):
    R[j] = un_list[m + 1 + j]

  i = 0
  j = 0
  k = l

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      un_list[k] = L[i]
      i = i + 1
    else:
      un_list[k] = R[j]
      j = j + 1
    k = k + 1

  while i < n1:
    un_list[k] = L[i]
    i = i + 1
    k = k + 1

  while j < n2:
    un_list[k] = R[j]
    j = j + 1
    k = k + 1

def merge_sort(un_list, l, r):
  if (l < r):
    m = l + (r-l)//2 # left + (right -left)//2
    merge_sort(un_list, l, m)
    merge_sort(un_list, m + 1, r)
    merge(un_list, l, m, r)

def main():
  unsorted_list = [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
  print('************ UNSORTED LIST **************')
  print(unsorted_list)
  n = len(unsorted_list)
  merge_sort(unsorted_list, 0, n-1)
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
