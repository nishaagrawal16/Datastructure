# ****************************************************
# Reverse a number either positive or negative
# O(n)
# ****************************************************


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 - 1 or x <= -2**31:
            return 0
        num1 = x
        sum = 0
        if x < 0:
            x = x *-1
        while(x):
            sum = sum * 10
            rem = x % 10
            x = x / 10
            sum = sum + rem
      
        if num1 < 0:
            sum = sum *-1
        if sum > 2**31 - 1 or sum <= -2**31:
            return 0
        return sum


def main():  
    s = Solution()
    print(s.reverse(-123))
    print(s.reverse(1463847412))
    print(s.reverse(1534236469))
    print(s.reverse(-2147483648))


if __name__ == '__main__':
    main()


# Input: 1463847412
# Expected: 2147483641
# 
# Input: 1534236469
# Expected: 0
# 
# Input: -2147483648
# Expected: 0
