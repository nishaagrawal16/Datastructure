# Date: 29-Jan-2020
# https://leetcode.com/problems/string-to-integer-atoi/
# O(n)

class Solution(object):
    def myAtoi(self, str1):
        '''
        :type str: str
        :rtype: int
        '''
        str1 = str1.strip()
        if not str1:
            return 0
        flag = False
        if str1[0] == '+' or str1[0] == '-':
            flag = True
            str2 = str1[1:]
        else:
            str2 = str1[:]
        if not str2:
            return 0        
        if not str2[0].isdigit(): # ABC #-ABC
            return 0
        for i in range(len(str2)): # 123, 123abc
            if str2.isdigit(): # 123, 231
                break
            if not str2[i].isdigit(): #-123Abc
                str2 = str2[:i]
                break    
        # Check sign(+ or -) is present
        if flag:
            str3 = str1[0] + str2
        else:
            str3 = str2[:]

        # Check for max and min values
        if int(str3) > 2**31 - 1:
            return 2**31 - 1
        elif int(str3) < -2**31:
            return -2**31
        else:
            return int(str3)


def main():
    s = Solution()
    print(':', s.myAtoi(''))
    print(' : ', s.myAtoi(' '))
    print('+: ', s.myAtoi('+'))
    print('   +   :', s.myAtoi('   +   '))
    print('    +123: ', s.myAtoi('    +123'))
    print('123     : ',s.myAtoi('123     '))
    print('-123: ', s.myAtoi('-123'))
    print('    +123ABC: ', s.myAtoi('    +123ABC'))
    print('-123ABC: ', s.myAtoi('-123ABC'))
    print('A123: ', s.myAtoi('A123'))
    print('78557565656123: ', s.myAtoi('78557565656123'))
    print('+78557565656123: ', s.myAtoi('+78557565656123'))
    print('-78557565656123: ', s.myAtoi('-78557565656123'))
    print('785ABC57565656123: ', s.myAtoi('785ABC57565656123'))
    print('4193 with words: ', s.myAtoi('4193 with words'))
    print('words and 987: ', s.myAtoi('words and 987'))
    print('-91283472332: ', s.myAtoi('-91283472332'))
    print('      -11919730356x: ', s.myAtoi('      -11919730356x'))


if __name__ == '__main__':
    main()

# Output:
# -------
# (':', 0)
# (' : ', 0)
# ('+: ', 0)
# ('   +   :', 0)
# ('    +123: ', 123)
# ('123     : ', 123)
# ('-123: ', -123)
# ('    +123ABC: ', 123)
# ('-123ABC: ', -123)
# ('A123: ', 0)
# ('78557565656123: ', 2147483647)
# ('+78557565656123: ', 2147483647)
# ('-78557565656123: ', -2147483648)
# ('785ABC57565656123: ', 785)
# ('4193 with words: ', 4193)
# ('words and 987: ', 0)
# ('-91283472332: ', -2147483648)
# ('      -11919730356x: ', -2147483648)
