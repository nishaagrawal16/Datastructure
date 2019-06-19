
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
      print(p.info, end=" ")
      p = p.next
    print('\n')

  def countNodes(self, linklist):
    p = linklist.start
    count = 0
    while p is not None:
      count = count + 1
      p = p.next
    return count

  def intersection(self, linkList1, linkList2):
    countl1 = self.countNodes(linkList1)
    countl2 = self.countNodes(linkList2)  
    print('count elements of list1: %s' % countl1)
    print('count elements of list2: %s' % countl2)
    l1 = linkList1.start
    l2 = linkList2.start
    if countl1 > countl2:
      d = countl1 - countl2
      while d > 0:
        l1 = l1.next
        d = d - 1
    else:
      d = countl2 - countl1
      while d > 0:
        l2 = l2.next
        d = d - 1
    print('Starting points: ', l1.info, l2.info)
    while l1.next is not None or l2.next is not None:
      if l1.next == l2.next:        
        print('intersection point: ', l1.next.info)
        return
      else:
        l1 = l1.next
        l2 = l2.next
    print('No intersection')


print('********** LIST-1 ***************')
linkList1 = LinkList()
linkList1.create_list([10,20,30,40,50])
linkList1.traverse()
print('********** LIST-2 ***************')
linkList2 = LinkList()
n1 = Node(15)
linkList2.start = n1
p = linkList2.start
n2 = Node(18)
p.next = n2
n2.next = linkList1.start.next
linkList2.traverse()
linkList1.intersection(linkList1, linkList2)