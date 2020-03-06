# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# https://leetcode.com/problems/jump-game-ii/
# O(n*m)

class Solution:
    def minimumSteps(self, nums):
        if len(nums) <= 1:
            return 0
        steps = 0
        i = 0
       
        while i < len(nums) - 1:
             # Check element with length (Last element)
            if nums[i] >= len(nums) - 1 - i:
                steps += 1
                return steps
            next_index = 0
            max_value = 0
            # if value of element is greater than 1, we need to find the max of values.
            if nums[i] > 1:
                for j in range(1, nums[i]+1):
                    index = i + j
                    # Check max value of following values + index
                    # [1, 5, 2, 3, 1, 1, 1]
                    # [0, 1, 2, 3, 4, 5, 6] = index
                    # [1, 5, 4, 6, 5, 6, 7] = Sum of nums[i+j] + (i+j)
                    if index < len(nums) and (nums[index] + index) > max_value:
                        next_index = j
                        max_value = nums[index] + index                  
            steps += 1
            if max_value:
                i = i + next_index
            else:
                i = i + 1
        return steps


def main():
    s = Solution()
    # nums = [2, 3, 1, 1, 4]
    # nums = [2, 1, 2, 3]
    # nums = [1, 1, 2, 3,1, 2]
    # nums =[3,2,1]
    nums =[1,2,1,1,1]
    #nums = [1, 5, 2, 3, 1, 1, 1]
    print(s.minimumSteps(nums))

if __name__ == '__main__':
    main()