# Date: 28-Jan-2020
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Examples
# 
# Input: 121
# Output: true
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Coud you solve it without converting the integer to a string?
# O(n)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        sum = 0
        if x < 0:
            return False
        while(x):
          sum = sum * 10
          rem = x % 10
          x = x / 10
          sum = sum + rem
        if sum == num:
            return True
        return False

def main():  
    s = Solution()
    print(s.isPalindrome(-121))
    print(s.isPalindrome(121))
    print(s.isPalindrome(10))

if __name__ == '__main__':
    main()
