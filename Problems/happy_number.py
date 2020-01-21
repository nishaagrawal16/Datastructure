# ****************************************************
# Find Given Number is Happy Number or not
# Number will be Happy when sum of it's digits square is 1
# ****************************************************

class Solution(object):
  def happy_number(self, num, list1):
    if num == 1:
      return 'Happy Number'
    no = [i for i in str(num)]
    sum = 0
    for i in no:
      sum = sum + int(i)**2

    if sum not in list1:
      list1.append(sum)
      print 'sum:{} list:{}'.format(sum, list1)
    else:
      print 'sum: ', sum
      return 'Not Happy Number'
    return self.happy_number(sum, list1)

def main():  
  s = Solution()
  list1 = []
  pr = s.happy_number(123, list1)
  print(pr)

if __name__ == '__main__':
  main()