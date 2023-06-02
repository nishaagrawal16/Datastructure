"""
https://leetcode.com/problems/longest-palindromic-substring/

Complexity
----------
O(n^2)
"""

class Solution:
  def checkPalindrome(self, s, l, r, start, end):
    while l >= 0 and r < len(s) and s[l] == s[r]:
      if end - start < r - l:
        start, end = l, r
      l -= 1
      r += 1
    return (start, end)

  def longestPalindrome(self, s: str) -> str:
    start = 0
    end = 0
    for i in range(len(s)):
      # ODD
      start, end = self.checkPalindrome(s, i-1, i+1, start, end)
      # Even
      start, end = self.checkPalindrome(s, i, i+1, start, end)
    return s[start: end + 1]

def main():
  s = Solution()
  input = 'babad'
  print('Input: ', input)
  output = s.longestPalindrome(input)
  print('Output : ', output)


if __name__ == '__main__':
  main()

# Output:
#---------
# Input:  babad
# Output :  bab
