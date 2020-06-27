# Date: 20-Jan-2020
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# Bubble Sort is the simplest sorting algorithm that works by
# repeatedly swapping the adjacent elements if they are in wrong order.
# Once the first pass completed last element will be sorted.
# On next pass, we need to compare till last-1 elements and in next pass
# last-2,...so on
# Example:
# list:  [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
# Pass1: [5, 6, 8, 1, 4, 9, 3, 2, 7, 10]
#                                    ---- Sorted
# Pass2: [5, 6, 1, 4, 8, 3, 2, 7, 9, 10]
#                                -------- Sorted
# .... So on
# Time Complexity: O(n2)
# Space Complexity: O(1)

def bubble_sort(un_list):
  n = len(un_list)
  for i in range(n):
    for j in range(n-1-i):
      if un_list[j] > un_list[j+1]:
        un_list[j+1], un_list[j] = un_list[j], un_list[j+1]

def main():
  unsorted_list = [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
  print('************ UNSORTED LIST **************')
  print(unsorted_list)
  bubble_sort(unsorted_list)
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
