# Remove duplicacy in unsorted list
# O(n)

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
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
      print('%d -> ' % p.info, end='')
      p = p.next
    print('None')

  def remove_duplicate_elements(self):
    p = self.start
    unique_list = set()
    if p is not None:
      unique_list.add(p.info)
    while p.next is not None:
      if p.next.info in unique_list:
        p.next = p.next.next
      else:
        unique_list.add(p.next.info)
        p = p.next

link_list = SingleLinkList()
link_list.create_list([5,1,7,1,2,5,3,7])
link_list.traverse()
print('****** AFTER REMOVE DUPLICATE ELEMENTS *********')
link_list.remove_duplicate_elements()
link_list.traverse()
