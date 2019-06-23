# Find intersection point of two sorted link list
# O(m+n)
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

  def countNodes(self):
    p = self.start
    count = 0
    while p is not None:
      count = count + 1
      p = p.next
    return count

  def intersection(self, link_list_1, link_list_2):
    count_l1 = link_list_1.countNodes()
    count_l2 = link_list_2.countNodes()
    print('count elements of list1: %s' % count_l1)
    print('count elements of list2: %s' % count_l2)
    l1 = link_list_1.start
    l2 = link_list_2.start
    if count_l1 > count_l2:
      d = count_l1 - count_l2
      while d > 0:
        l1 = l1.next
        d = d - 1
    else:
      d = count_l2 - count_l1
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

def main():
  print('********** LIST-1 ***************')
  link_list_1 = LinkList()
  link_list_1.create_list([10,20,30,40,50])
  link_list_1.traverse()
  print('********** LIST-2 ***************')
  link_list_2 = LinkList()
  n1 = Node(15)
  link_list_2.start = n1
  p = link_list_2.start
  n2 = Node(18)
  p.next = n2
  n2.next = link_list_1.start.next
  link_list_2.traverse()
  link_list_1.intersection(link_list_1, link_list_2)

if __name__ == '__main__':
  main()

# Output
# -------
# ********** LIST-1 ***************
# 10 ->  20 ->  30 ->  40 ->  50 ->  None
# ********** LIST-2 ***************
# 15 ->  18 ->  20 ->  30 ->  40 ->  50 ->  None
# count elements of list1: 5
# count elements of list2: 6
# Starting points:  10 18
# intersection point:  20
