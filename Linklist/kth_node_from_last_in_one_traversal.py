#!/usr/bin/python

# Date: 2019-06-22
#
# Description:
# Find kth element from last in a singly linked list.
#
# Approach:
# Take 2 pointers p1 and p2, move p1 to kth node from beginning and p2 at head.
# Now iterate over linked list until p1 reaches end. When p1 reaches end p2
# will be k nodes behind which is kth from last.
#
# Complexity:
# O(n) Time

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

  def kthElementFromLast(self, k):
    p1 = self.start
    p2 = self.start
    i = 1
    while p1 is not None and i <= k:
      p1 = p1.next
      i = i + 1
    # Now p1 is at kth position from head and p2 is at starting/head.
    # Iterate over linked list until p1 reaches end, when p1 will reach end, p2
    # will be at (n - k) position, which is kth from last.
    while p1 is not None:
      p1 = p1.next
      p2 = p2.next
    print('%d element from the last: %d' % (k, p2.info))

def main():
  print ('*************** LIST-1 ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([1, 3, 5, 10, 50, 30, 4, 6, 9, 22])
  link_list_1.traverse()
  link_list_1.kthElementFromLast(3)

if __name__ == '__main__':
  main()

# Output
# -------
# *************** LIST-1 ***********************
# 1 -> 3 -> 5 -> 10 -> 50 -> 30 -> 4 -> 6 -> 9 -> 22 -> None
# 3 element from the last: 6