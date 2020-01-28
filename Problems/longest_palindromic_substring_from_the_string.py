# Date: 27-Jan-2020
# Find the longest palindrome substring from the given string.
# https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
# We need to do check both even and odd palindrome.
# O(n2)
# Need to find different approach of O(n)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_length = 1
        start = 0
        low = 0
        high = 0
        for i in range(1, n):
            # For even palindrome, we need to take adjacent numbers.
            low = i - 1
            high = i
            start, max_length = self.check_max_palindrome(s, low, high, n, max_length, start)
            # For odd palindrome
            low = i - 1
            high = i + 1
            start, max_length = self.check_max_palindrome(s, low, high, n, max_length, start)
        return s[start: start + max_length]

    def check_max_palindrome(self, s, low, high, n, max_length, start):
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low = low - 1
            high = high + 1
        return start, max_length            

def main():
    s = 'abybadfkjhdgfabbaf'
    sol = Solution()
    print(sol.longestPalindrome(s))

if __name__ == '__main__':
    main()
