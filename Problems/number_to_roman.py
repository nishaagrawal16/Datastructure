#!/usr/bin/python

# Date: 2022-10-26
#
# Problem: https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num:
            res += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res




def main():
    s = Solution()
    for n in [3, 58, 123, 1994]:
        print('%d: %s' % (n, s.intToRoman(n)))

if __name__ == '__main__':
    main()

# Output
# ------
# 3: III
# 58: LVIII
# 123: CXXIII
# 1994: MCMXCIV
