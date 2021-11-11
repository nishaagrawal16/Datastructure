# Remove duplicate elements from sorted array
# Time Complexity O(n)
# Space complexity O(1)

class Solution:
    def removeDuplicates(self, nums):
        # Maintain a index for counting and placing the distinct element.
        i = 0
        for j in range(1, len(nums)):
            # If elements are not equal, place the unique value to the next position.
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        i += 1
        return i

s = Solution()
n = [1, 2, 2, 3, 3, 3, 4]
print('Initial list: ', n)
new_length = s.removeDuplicates(n)
print('total distinct elements in the list: ', new_length)
print('Inplace modified list:', n)

Output:
-------
Initial list:  [1, 2, 2, 3, 3, 3, 4]
total distinct elements in the list:  4
Inplace modified list: [1, 2, 3, 4, 3, 3, 4]
