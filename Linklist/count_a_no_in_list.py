#!/usr/bin/python

# Count a number is present how many times in the link list.
class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class LinkList:
  def __init__(self):
    self.start = None

  def create_list(self, li):
    if self.start is None:
      self.start = Node(li[0])
    p = self.start
    i = 1
    while i < len(li):
      temp = Node(li[i])
      p.next = temp
      p = p.next
      i = i + 1

  def traverse(self):
    p = self.start
    i = 0
    while p is not None and i<10:
      print('%d ->' % p.info, end=" ")
      p = p.next
      i = i + 1
    print('None')

  def countANumber(self, num):
    count = 0
    if self.start is None:
      print('List is Empty')
      return count
    p = self.start
    while p is not None:
      if p.info == num:
        count = count + 1
      p = p.next
    return count

def main():
  num = int(input('Enter number of Nodes in the link list: '))
  link_list = []
  i = 0
  while i < num:
    ele = int(input('Enter %d element: ' % i))
    link_list.append(ele)
    i = i + 1

  linkList = LinkList()
  linkList.create_list(link_list)
  linkList.traverse()
  count_num = int(input('Enter a number: '))
  count = linkList.countANumber(count_num)
  print('Number of times value %s present in list: %s' % (count_num, count))

if __name__ == '__main__':
  main()

# Output:
# -------
# Enter number of Nodes in the link list: 4
# Enter 0 element: 1
# Enter 1 element: 3
# Enter 2 element: 2
# Enter 3 element: 1
# 1 -> 3 -> 2 -> 1 -> None
# Enter a number: 1
# Number of times value 1 present in list: 2
