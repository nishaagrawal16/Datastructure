# Date: 20-Jan-2020
# https://www.geeksforgeeks.org/python-program-for-quicksort/#

# In quick sort, Target of partitions is, given an array and
# an element x of array as pivot, put x at its correct position
# in sorted array and put all smaller elements (smaller than x) before x,
# and put all greater elements (greater than x) after x.
# All this should be done in linear time.
# O(nlogn) average case
# If the array is already sorted and we take the last element as pivot. worst
# case complexity: O(n2)

def partition(un_list, low, high):
  i = low - 1

  # Select the last element as pivot.
  pivot = un_list[high]
  for j in range(low, high):
    # Elements which are less than pivot will placed from starting of the list.
    if un_list[j] <= pivot:
      i = i + 1
      un_list[i], un_list[j] = un_list[j], un_list[i]
  # Set pivot after the smaller sequence.
  un_list[i+1], un_list[high] = un_list[high], un_list[i+1]
  return i+1

def quick_sort(un_list, low, high):
  if (low < high):
    pi = partition(un_list, low, high)
    quick_sort(un_list, low, pi-1)
    quick_sort(un_list, pi+1, high)

def main():
  unsorted_list = [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
  print('************ UNSORTED LIST **************')
  print(unsorted_list)
  n = len(unsorted_list)
  quick_sort(unsorted_list, 0, n-1)
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
