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
    for i in range(1,len(li)):
      temp = Node(li[i])
      p.next = temp
      p = p.next

  def traverse(self):
    p = self.start
    while p is not None:
      print(p.info, end=" ")
      p = p.next
    print('\n')

  def prepareEvenOdd(self):
    p = self.start
    count = 0
    even = 0
    odd = 0
    # check all even or all odd
    while p is not None:
      if p.info % 2 == 0:
        even = even + 1
      else:
        odd = odd + 1
      count = count + 1
      p = p.next 
    if even == count or odd == count:
      return
    p = self.start
    q = self.start
    # point q to the last element for adding the odd elements on trail
    while q.next is not None:
      q = q.next
    prev = None
    last = q
    # End loop while p reaches to last otherwise loop will go on infinity times
    while p.next is not None and p != last:
      if p.info % 2 != 0:
        # First element can be odd, so check prev also
        if prev is None:          
          q.next = p
          self.start = p.next
        else:
          q.next = prev.next
          prev.next = p.next
        p = p.next
        q = q.next        
        q.next = None
      else:        
        prev = p
        p = p.next
    print ('Last element of list: ', p.info)

linkList = LinkList()
linkList.create_list([17, 15, 8, 12, 10, 5, 4, 1, 7, 6])
# linkList.create_list([8, 12, 10, 5, 4, 1,6])
# linkList.create_list([8, 12, 10])
# linkList.create_list([1, 3, 5, 7])
linkList.traverse()
linkList.prepareEvenOdd()
linkList.traverse()