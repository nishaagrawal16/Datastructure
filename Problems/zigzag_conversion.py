# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:# 
# string convert(string s, int numRows);
# https://www.geeksforgeeks.org/print-concatenation-of-zig-zag-string-form-in-n-rows/
# O(len)
# length of string


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not numRows:
            return '0 numRows'
        if numRows == 1:
            return s
        arr = ['' for i in range(numRows)]
        row = 0
        for i in range(len(s)):
            arr[row] += s[i]
            if row == numRows - 1:
                down = False
            if row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1
        return ''.join(arr)


def main():
    s = Solution()
    output_str = s.convert('PAYPALISHIRING', 3)
    print(output_str)

if __name__ == '__main__':
    main()

# Output:
#--------
# PAHN
# APLSIIG
# YIR
