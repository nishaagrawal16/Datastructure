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
  l3.start = temp
  p = l3.start

  while p1 is not None and p2 is not None:
    if p.info != p1.info or p.info != p2.info:      
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
      p.next = temp
      p = p.next
    else:
      if p.info == p1.info:
        p1 = p1.next
      elif p.info == p2.info:
        p2 = p2.next
  # Push remaining nodes of list1 to list3
  if p1 is not None:
    p = Node(p1.info)
    p1 = p1.next
    p = p.next
  # Push remaining nodes of list2 to list3
  if p2 is not None:
    temp = Node(p2.info)
    p.next = temp
    p2 = p2.next
    p = p.next
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

def union_new(l1, l2):
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
  if p1 is not None:
    p = Node(p1.info)
    p1 = p1.next
    p = p.next
  # Push remaining nodes of list2 to list3
  if p2 is not None:
    temp = Node(p2.info)
    p.next = temp
    p2 = p2.next
    p = p.next
  print('*********** UNION OF LISTS *******************')
  l3.traverse()
def main():
  print ('*************** LIST-1 ***********************')
  linkList1 = LinkList()
  linkList1.create_list([1, 3, 5])
  linkList1.traverse()
  print ('*************** LIST-2 ***********************')
  linkList2 = LinkList()
  linkList2.create_list([1, 4, 5, 6])
  linkList2.traverse()

  union(linkList1, linkList2)
  intersection(linkList1, linkList2)
  union_new(linkList1, linkList2)

if __name__ == '__main__':
  main()