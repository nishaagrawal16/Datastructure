# Merge two sorted linklist with duplicate data.
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
      # Add both nodes to temp
      temp = Node(p1.info)
      temp2 = Node(p2.info)
      temp.next = temp2
      p1 = p1.next
      p2 = p2.next 
    if l3.start is None:
      l3.start = temp
      p_l3 = l3.start
    else:
      p.next = temp
      p_l3 = p.next
    while p_l3.next is not None:
      p_l3 = p_l3.next
    p = p_l3

  # Push remaining nodes of list1 to list3
  while p1 is not None:
    temp = Node(p1.info)
    p.next = temp
    p1 = p1.next
    p = p.next
  # Push remaining nodes of list2 to list3
  while p2 is not None:
    temp = Node(p2.info)
    p.next = temp
    p2 = p2.next
    p = p.next
  print('*********** UNION OF LISTS *******************')
  l3.traverse()

def main():
  print ('*************** LIST-1 ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([1, 3, 5, 10, 20, 20, 30])
  link_list_1.traverse()
  print ('*************** LIST-2 ***********************')
  link_list_2 = LinkList()
  link_list_2.create_list([1, 4, 4, 5, 6, 10])
  link_list_2.traverse()
  union(link_list_1, link_list_2)

if __name__ == '__main__':
  main()

# Output:
# -------
# *************** LIST-1 ***********************
# 1 -> 3 -> 5 -> 10 -> 20 -> 20 -> 30 -> None
# *************** LIST-2 ***********************
# 1 -> 4 -> 4 -> 5 -> 6 -> 10 -> None
# *********** UNION OF LISTS *******************
# 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 5 -> 6 -> 10 -> 10 -> 20 -> 20 -> 30 -> None
