"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Sliding window
Complexity
----------
O(n)
"""
from collections import Counter

class Solution:
  def lengthOfLongestSubstring(self, s):
    res = 0
    left = right = 0
    chars = Counter()
    while right < len(s):
      r = s[right]
      chars[r] += 1

      while chars[r] > 1:
        l = s[left]
        chars[l] -= 1
        left += 1

      res = max(res, right - left + 1)
      right += 1
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
