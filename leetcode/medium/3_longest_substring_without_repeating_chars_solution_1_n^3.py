"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Complexity
----------
O(n^3)
"""

class Solution:
  def lengthOfLongestSubstring(self, s):
    if len(s) == 1:
      return 1
    nonRepeating = []
    result = []
    for i in range(len(s)):
      for j in range(i, len(s)):
        if s[j] not in nonRepeating:
          nonRepeating.append(s[j])
        else:
          result.append(''.join(nonRepeating))
          nonRepeating = []
          break
    val = ''
    for item in result:
      if len(val) < len(item):
        val = item
    return len(val)

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
