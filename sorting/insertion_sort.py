# Date: 20-Jan-2020
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
#
# In insertion sort, we need to start from index 1 and check the previous indexes
# that they are in the sorting order or not. If previous index's value is smaller than current key.
# swap the elements and goes to the previous element of left.
# On 1st pass, we need to compare 1st element to the 0th and
# in next pass 2nd, we need to comapre 2nd element to 1st and 0th,...so on
# Example:
# list:  [8, 5--, 6, 9, 1, 4, 10, 3, 2, 7]
# Pass1: [5, 8, 6--, 9, 1, 4, 10, 3, 2, 7]
# Sorted----
# Pass2: [5, 6, 8, 9--, 1, 4, 10, 3, 2, 7]
# Sorted -----
# .... So on
# O(n2)

def insertion_sort(un_list):
  n = len(un_list)
  for i in range(1, n):
    key = un_list[i]
    j = i - 1
    while (j>=0 and key < un_list[j]):
      un_list[j+1] = un_list[j]
      j = j - 1
    un_list[j+1] = key


def main():
  unsorted_list = [8, 5, 6, 9, 1, 4, 10, 3, 2, 7]
  print('************ UNSORTED LIST **************')
  print(unsorted_list)
  insertion_sort(unsorted_list)
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
