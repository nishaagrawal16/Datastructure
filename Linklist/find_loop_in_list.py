# Check whether Loop is present or not
# Total Element present in loop

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class LinkList:
  def __init__(self):
    self.start = None
    
  def create_list_with_loop(self):
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    # n6 = Node(60)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    #n5.next = n6
    n5.next = n2
    self.start = n1

  def traverse(self):
    p = self.start
    i = 0
    while p is not None and i<10:
      print('%d -> ' % p.info, end=" ")
      p = p.next
      i = i + 1
    print('None')

  def findLoopWithTotalElementsInLoop(self):
    slow = self.start
    fast = self.start
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        print('Loop present at', slow.info)
        slow = slow.next
        count = 1
        while slow != fast:
          count = count + 1
          slow = slow.next
        return count
    print('No Loop present')
    return 0
   
link_list = LinkList()
link_list.create_list_with_loop()
link_list.traverse()
count = link_list.findLoopWithTotalElementsInLoop()
print('Total Nodes present in loop: %s' % count)
