# Find sum of a[i]%a[j] for all valid pairs
# https://www.geeksforgeeks.org/find-sum-of-aiaj-for-all-valid-pairs/
# li is unsorted
# Input: arr[] = {1, 2, 3}
# Output: 5
# (1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2)
# + (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5
# O(k^2) where k is the hightest number

class Solutions:
  def sum_of_mod(self, li):
    count = [0]*(max(li) + 1)
    # Maintain count of each element
    for i in li:
      count[i] += 1
    result = 0
    print('Occurance of elements: ', count)
    # We skip i = 0 and j = 0  because 0 value does not give any result
    # Means 0%n = 0
    for i in range(1, len(count)):
      for j in range(1, len(count)):
        # print(i, j, count[i], count[j])
        # i%j with multiply the occurance of numbers.
        result += count[i]*count[j]*(i%j)
    return result


def main():
  s = Solutions()
  array = [1, 2, 4, 4, 4]
  print('Array: ', array)
  print('Sum of modulus of each pair: ', s.sum_of_mod(array))

if __name__ == '__main__':
  main()


# Output:
# -------
# Array:  [1, 2, 4, 4, 4]
# Occurance of elements:  [0, 1, 1, 0, 3]
# Sum of modulus of each pair:  10

