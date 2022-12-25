# Remove duplicacy in sorted link list.
# O(n)

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None

  def create_list(self):
    n1 = Node(1)
    n2 = Node(1)
    n3 = Node(2)
    n4 = Node(3)
    n5 = Node(3)
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

  def remove_duplicate_elements(self):
    p = self.start
    while p.next is not None:
      if p.info == p.next.info:
        p.next = p.next.next
      else:
        p = p.next

link_list = SingleLinkList()
link_list.create_list()
link_list.traverse()
print('****** AFTER REMOVE DUPLICATE ELEMENTS *********')
link_list.remove_duplicate_elements()
link_list.traverse()

# Output:
# -------
# 1 ->  1 ->  2 ->  3 ->  3 ->  None
# ****** AFTER REMOVE DUPLICATE ELEMENTS *********
# 1 ->  2 ->  3 ->  None
