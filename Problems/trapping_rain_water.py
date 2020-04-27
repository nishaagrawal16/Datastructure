# https://leetcode.com/problems/trapping-rain-water/
# Take the maximum right of the array element
# find max left of each element and min(left_max, right_max[i]) - height[i]
# O(n)
class Solution:
    def trap(self, height):
        if len(height) == 0:
            return 0
        right_max = [0]*len(height)
        i = len(height) - 1
        right_max[i] = height[i]
        i -= 1
        while i>= 0:
            right_max[i] = max(height[i], right_max[i+1])
            i -= 1
        left_max = 0
        i = 0
        amount_of_water = 0
        while i < len(height):
            left_max = max(left_max, height[i])
            amount_of_water += min(left_max, right_max[i]) - height[i]            
            i += 1
        return amount_of_water


def main():
    s = Solution()
    height =  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))


if __name__ == '__main__':
    main()
