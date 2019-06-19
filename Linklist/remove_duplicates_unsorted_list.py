class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None

  def create_list(self):
    n1 = Node(5)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(1)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    self.start = n1

  def traverse(self):
    p = self.start
    while p is not None:
      print(p.info, end=" ")
      p = p.next
    print('\n')

  def remove_duplicate_elements(self):
    p = self.start
    unique_dict = {}
    if p is not None:
      unique_dict[p.info] = True
    while p.next is not None:
      if unique_dict.get(p.next.info):
        p.next = p.next.next
      else:
        unique_dict[p.next.info] = True
        p = p.next

linkList = SingleLinkList()
linkList.create_list()
linkList.traverse()
print('****** AFTER REMOVE DUPLICATE ELEMENTS *********')
linkList.remove_duplicate_elements()
linkList.traverse()
