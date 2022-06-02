# https://leetcode.com/problems/divide-two-integers/
# TODO

class Solution:
    def divide(self, dividend, divisor):
        print(2**31, dividend)

        # print('dividend: ', dividend, divisor)
        divisor_neg_flag = False
        dividend_neg_flag = False
        new_divisor = divisor
        new_dividend = dividend

        if divisor < 0 and dividend < 0:
            new_divisor = -1*divisor
            new_dividend = -1*dividend

        if divisor < 0 and dividend > 0:
            new_divisor = -1*divisor
            divisor_neg_flag = True

        if divisor > 0 and dividend < 0:
            new_dividend = -1*dividend
            dividend_neg_flag = True

        print('new_dividend: ', new_dividend, new_divisor)
        if not (-2**31 <= new_divisor <= 2**31 -1 and -2**31 <= new_dividend <= 2**31 -1):
            print('yes')
            return 2**31 - 1
        print('dividend_neg_flag: ', dividend_neg_flag)
        if new_divisor == 1:
            if divisor_neg_flag or dividend_neg_flag:
                print('new_dividend: ', new_dividend, dividend)
                return -1*new_dividend
            else:
                return dividend
        i = 0
        sum_of_divisor = 0
        result = 0
        # print('sum_of_divisor: ', sum_of_divisor)
        # print('dividend: ', dividend)
        # print('new_divisor: ', new_divisor)
        while sum_of_divisor < new_dividend:
            sum_of_divisor += new_divisor
            if sum_of_divisor > new_dividend:
                break
            result += 1
        # print('result: ', result)
        if divisor_neg_flag or dividend_neg_flag:
            return -1*result
        else:
            return result

def main():
    s = Solution()
    # result = s.divide(-2147483648, -1)
    result = s.divide(-1, 1)

    print('Answer: ', result)

if __name__ == '__main__':
    main()
