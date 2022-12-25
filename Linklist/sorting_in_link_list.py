# Date: 13-Feb-2020
# Sorting in linklist using bubble sort
# O(n2)

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None

  def create_list(self):
    n1 = Node(30)
    n2 = Node(10)
    n3 = Node(40)
    n4 = Node(5)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    self.start = n1

  def traverse(self):
    p = self.start
    while p is not None:
      print('%d -> ' % p.info, end='')
      p = p.next
    print('None')

  def countNodes(self):
    p = self.start
    count = 0
    while p is not None:
      count = count + 1
      p = p.next
    print('Total Nodes: ', count)
    return count

  def bubble_sort(self):
    if self.start is None:
        return
    count = self.countNodes()
    for i in range(count):
      swap = 0
      p = self.start
      q = p.next
      prev = None
      while p is not None and q is not None:
        if p.info > q.info:
          swap = 1
          p.next = q.next
          q.next = p
          if prev is None:
            self.start = q
            p = self.start
          else:
            prev.next = q
          prev = q
          q = p.next
        else:
          prev = p
          p = p.next
          q = q.next
      if swap == 0:
          break
      self.traverse()

link_list = SingleLinkList()
print('*********** CREATING LIST ***************')
link_list.create_list()

print('*********** TRAVERSE LIST ***************')
link_list.traverse()
link_list.bubble_sort()
print('*********** SORTED LIST ***************')
link_list.traverse()

