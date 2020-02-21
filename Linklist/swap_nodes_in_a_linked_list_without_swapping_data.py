# All data in the link_list is unique
# SWAP x, Y
# Swap all pairs
# move-last-element-to-front-of-a-given-linked-list

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
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n6 = Node(60)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    self.start = n1

  def traverse(self):
    p = self.start
    while p is not None:
      print('%d -> ' % p.info, end=" ")
      p = p.next
    print('None')

  def swap(self, x, y):
    # when x and y are same number
    if x == y:
      return

    prevX = None
    currX = self.start
    while currX is not None and currX.info != x:
      prevX = currX
      currX = currX.next

    prevY = None
    currY = self.start
    while currY is not None and currY.info != y:
      prevY = currY
      currY = currY.next      
    
    # If any x or y is not present in the list
    if currX == None or currY == None:
      return
    # If x is not head of linked list 
    if prevX != None:
      prevX.next = currY
    else:
      self.start = currY
    # If y is not head of linked list 
    if prevY != None:
      prevY.next = currX
    else:
      self.start = currX

    temp = currX.next
    currX.next = currY.next
    currY.next = temp

  def swapAllPairs(self):
    p = self.start
    while p is not None and p.next is not None:
      temp = p.next.info
      p.next.info = p.info
      p.info = temp
      p = p.next.next

  def moveLastElementToFirst(self):
    prev = None
    curr = self.start
    while curr.next is not None:
      prev = curr
      curr = curr.next

    curr.next = self.start
    self.start = curr
    prev.next = None


link_list = LinkList()
link_list.create_list()
link_list.traverse()
print ('************SWAP 20 and 40 ********************')
link_list.swap(20,40)
#link_list.swap(10,20)
#link_list.swap(20,400)
link_list.traverse()
print ('************SWAP all pairs data ***************')
link_list.swapAllPairs()
link_list.traverse()
print ('************ Move last element to first *******')
link_list.moveLastElementToFirst()
link_list.traverse()