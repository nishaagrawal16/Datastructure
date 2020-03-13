# ****************************************************
# Find Given Number is Happy Number or not
# Number will be Happy when sum_of_sq_digit of it's digits square is 1
# https://www.geeksforgeeks.org/happy-number/
# ****************************************************

class Solution(object):
  def happy_number(self, num, list1):
    if num == 1:
      return 'Happy Number'
    no = [i for i in str(num)]
    sum_of_sq_digit = 0
    for i in no:
      sum_of_sq_digit = sum_of_sq_digit + int(i)**2

    if sum_of_sq_digit not in list1:
      list1.append(sum_of_sq_digit)
      print('sum_of_sq_digit:{} list:{}'.format(sum_of_sq_digit, list1))
    else:
      print('sum_of_sq_digit: ', sum_of_sq_digit)
      return 'Not Happy Number'
    return self.happy_number(sum_of_sq_digit, list1)

def main():
  s = Solution()
  list1 = []
  pr = s.happy_number(123, list1)
  print(pr)

if __name__ == '__main__':
  main()