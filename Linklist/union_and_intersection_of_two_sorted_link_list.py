# Union of two sorted linklist
# Intersection of two sorted linklist
# o(m+n)
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
      print('%d ->' % p.info, end=" ")
      p = p.next
    print ('None')

def union(l1, l2):
  p1 = l1.start
  p2 = l2.start
  l3 = LinkList()
  while p1 is not None and p2 is not None:
    if p1.info < p2.info:
      temp = Node(p1.info)
      p1 = p1.next
    elif p1.info > p2.info:
      temp = Node(p2.info)
      p2 = p2.next
    else:
      temp = Node(p1.info)
      p1 = p1.next
      p2 = p2.next 
    if l3.start is None:
      l3.start = temp
      p = l3.start
    elif temp.info != p.info:
      p.next = temp
      p = p.next

  # Push remaining nodes of list1 to list3
  while p1 is not None:
    if p1.info != p.info:
      temp = Node(p1.info)
      p.next = temp
      p = p.next
    p1 = p1.next
  # Push remaining nodes of list2 to list3
  while p2 is not None:
    if p2.info != p.info:
      temp = Node(p2.info)
      p.next = temp
      p = p.next
    p2 = p2.next
  print('*********** UNION OF LISTS *******************')
  l3.traverse()

def intersection(l1, l2):
  p1 = l1.start
  p2 = l2.start
  l3 = LinkList()
  while p1 is not None and p2 is not None:
    if p1.info < p2.info:
      p1 = p1.next
    elif p1.info > p2.info:
      p2 = p2.next
    else:
      temp = Node(p1.info)
      if l3.start == None:        
        l3.start = temp
        p = l3.start
      elif p1.info != p.info:
        p.next = temp
        p = p.next
      p1 = p1.next
      p2 = p2.next
  print('*********** INTERSECTION OF LISTS *******************')
  l3.traverse()

def main():
  print ('*************** LIST-1 ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([1, 3, 5, 10, 10, 30])
  link_list_1.traverse()
  print ('*************** LIST-2 ***********************')
  link_list_2 = LinkList()
  link_list_2.create_list([1, 4, 4, 5, 6])
  link_list_2.traverse()

  union(link_list_1, link_list_2)
  intersection(link_list_1, link_list_2)

if __name__ == '__main__':
  main()