# ****************************************************
# Reverse a number either positive or negative
# O(n)
# ****************************************************

class Solution(object):
  def reverse_number(self, num):
    num1 = num
    sum = 0
    if num < 0:
      num = num *-1
    while(num):
      sum = sum*10
      rem = num%10
      num = num/10
      sum = sum + rem

    if num1 < 0:
      sum = sum *-1
    return sum


def main():  
  s = Solution()
  print(s.reverse_number(-123))
  print(s.reverse_number(345))

if __name__ == '__main__':
  main()