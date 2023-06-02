"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Complexity
----------
O(n^2)
"""

class Solution:
  def lengthOfLongestSubstring(self, s):
    if len(s) == 1:
      return 1
    res = 0
    for i in range(len(s)):
      seen = set()
      for j in range(i, len(s)):
        seen.add(s[j])
        if len(seen) < j - i + 1:
          break
        res = max(res, j - i + 1)
    return res

def main():
  s = Solution()
  input = "abcabcbb"
  print('input = ', input)
  output = s.lengthOfLongestSubstring(input)
  print('Output : ', output)


if __name__ == '__main__':
  main()

# Output:
#---------
# input =  abcabcbb
# Output :  3
