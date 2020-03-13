# Need to solve it TODO
# +++++++++++++++++++

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return 0
        roman_dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',
                     500: 'D', 1000: 'M', 4: 'IV', 9:'IX', }
        if num in roman_dic.keys():
            return roman_dic[num]
        n = len(str(num))    
        mul = 1
        li = [0]*n
        i = n - 1
        while num > 0:
            rem = num % 10
            li[i] = rem * mul
            num = num/10
            mul = mul*10
            i = i - 1
        print(li)
        roman = ''
        for i in range(len(li)):
            if li[i] in roman_dic.keys():
                roman += roman_dic[li[i]]
            else:
                if li[i] < 4:
                    roman += 'I'*li[i]

                elif li[i] < 9:
                    roman += 'V'+ 'I'*(li[i] - 5)

                elif li[i] < 40:
                    roman += 'X' + ''*(li[i] - 5)
                elif li[i] < 90:

                elif li[i] < 400:

                elif li[i] < 900:





def main():
    s = Solution()
    print(':', s.intToRoman(123))

if __name__ == '__main__':
    main()