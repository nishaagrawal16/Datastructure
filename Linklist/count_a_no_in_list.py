# Count A number is present how many times in the link list
class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class LinkList:
  def __init__(self):
    self.start = None

  def create_list(self):
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(10)
    n4 = Node(40)
    n5 = Node(10)
    n6 = Node(10)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    self.start = n1

  def traverse(self):
    p = self.start
    i = 0
    while p is not None and i<10:
      print(p.info, end=" ")
      p = p.next
      i = i + 1
    print('\n')

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
linkList = LinkList()
linkList.create_list()
linkList.traverse()
count = linkList.countANumber(10)
print('Number of times value %s present in list: %s' % (10, count))