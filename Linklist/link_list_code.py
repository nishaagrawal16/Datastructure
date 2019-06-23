class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None

  def create_list(self):
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    self.start = n1

  def traverse(self):
    p = self.start
    while p is not None:
      print('%d -> ' % p.info, end=" ")
      p = p.next
    print('None')
    
  def searchElement(self, value):
    p = self.start
    pos = 1
    while p is not None:
      if p.info == value:
        print('element %s found at position %s' % (value, pos))
        return
      pos = pos + 1
      p = p.next
    print('element %s not present in the list' % value)

  def countNodes(self):
    p = self.start
    count = 0
    while p is not None:
      count = count + 1
      p = p.next
    print('Total Nodes: ', count)
    return count

  def insertAtBeg(self, value):
    temp = Node(value)
    if self.start is not None:
      temp.next = self.start
    self.start = temp

  def insertEnd(self, value):
    temp = Node(value)
    if self.start == None:
      self.start = temp
    else:
      p = self.start
      while p.next is not None:
        p = p.next
      p.next = temp

  def insertBetween(self, value, k):
    temp = Node(value)
    count = self.countNodes()
    if k > count:
      print('List is smaller than given number')
      return
    p = self.start
    travel = 1
    while p.next is not None and travel < k-1:
      p = p.next
      travel = travel + 1
    temp.next = p.next
    p.next = temp 
    
  def deleteEnd(self):
    if self.start == None:
      print('List is empty')
      return
    p = self.start
    while p.next.next is not None:
      p = p.next
    p.next = None

  def deleteFromBeg(self):
    if self.start == None:
      print('List is empty')
      return
    self.start = self.start.next

  def deleteFromBetween(self, k):
    if self.start == None:
      print('List is empty')
      return
    count = self.countNodes()
    if k > count:
      print('List is smaller than given number')
      return
    p = self.start
    travel = 1
    while p.next is not None and travel < k-1:
      p = p.next
      travel = travel + 1
    p.next = p.next.next

  def deleteAtInfo(self, value):
    if self.start == None:
      print('List is empty')
      return
    p = self.start
    found = False
    while p.next is not None:
      if p.next.info == value:
        found = True
        break;
      p = p.next
    if not found:
      print('element not found in the list')
      return
    p.next = p.next.next


  def nthNode(self, k):
    p = self.start
    temp = self.start
    length = 0
    while temp is not None:
      temp = temp.next
      length += 1
    if k > length:
      print('K is more than length of the link list')      
    i = 1
    while p is not None and i< k:
      i = i + 1
      p = p.next
    if p is not None:
      print('%sth element is: %s' % (k, p.info))

  def nthNodeFromLast(self, k):
    p = self.start
    temp = self.start
    length = 0
    while temp is not None:
      temp = temp.next
      length += 1
    newK = length - k + 1
    if newK > length:
      print('K is more than length of the link list')      
    i = 1
    while p is not None and i< newK:
      i = i + 1
      p = p.next
    if p is not None:
      print('%sth element is: %s' % (k, p.info))

  def middleElement(self):
    if not self.start:
      print('List is empty')
    slow = self.start
    fast = self.start
    while fast and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
    print('middle element is: ', slow.info)

  def reverse(self):
    prev =  None
    current = self.start
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.start = prev  

link_list = SingleLinkList()
print('*********** CREATING LIST ***************')
link_list.create_list()

print('*********** TRAVERSE LIST ***************')
link_list.traverse()

print('*********** SEARCHING ELEMENT ***********')
link_list.searchElement(20)

print('*********** COUNT NODES *****************')
count = link_list.countNodes()

print('*********** INSERT- AT BEGINING *********')
link_list.insertAtBeg(5)
link_list.traverse()

print('*********** INSERT- AT END **************')
link_list.insertEnd(55)
link_list.traverse()

print('*********** INSERT- AT Kth LOCATION *****')
link_list.insertBetween(25, 4)
link_list.traverse()

print('*********** DELETE- AT END **************')
link_list.deleteEnd()
link_list.traverse()

print('*********** DELETE- FROM BEGNING ********')
link_list.deleteFromBeg()
link_list.traverse()

print('*********** DELETE- AT Kth LOCATION *****')
link_list.deleteFromBetween(3)
link_list.traverse()

print('*********** DELETE- GIVEN INFO **********')
link_list.deleteAtInfo(30)
link_list.traverse()

print('*********** Nth NODE ********************')
link_list.nthNode(3)

# This is in two times traversal
print('*********** Nth NODE FROM LAST **********')
link_list.nthNodeFromLast(4)

print('*********** MIDDLE NODE *****************')
link_list.middleElement()

print('********** REVERSE LINK LIST ************')
link_list.reverse()
link_list.traverse()
