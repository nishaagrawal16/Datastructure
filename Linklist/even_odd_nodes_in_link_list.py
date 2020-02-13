# Find the even number of nodes and odd nombers of node
# Example:
# even, even, Odd, odd, odd, poditions

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
      print('%d -> ' % p.info, end=" ")
      p = p.next
    print('None')

  def oddEvenList(self):
    p = self.start
    q = self.start    
    while q.next is not None:
      q = q.next
    last = q
    prev = None
    i = 0
    # last != p is to reach to the last node.
    while p.next is not None and last != p:
      # Check for indexed
      if i%2 != 0:
        q.next = p
        prev.next = p.next
        q = q.next
        q.next = None
        p = prev.next
      else:
        prev = p
        p = p.next
      i = i + 1


link_list = LinkList()
link_list.create_list([1, 2, 3, 4, 5])
# Expected: 1, 3, 5, 2, 4
link_list.traverse()
link_list.oddEvenList()
print('************* ODD-EVEN LIST **************')
link_list.traverse()
