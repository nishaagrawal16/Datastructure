#!/usr/bin/python

# Date: 2018-09-17
#
# Description:
# There is a linked list given and a value x, partition a linked list such that
# all element less x appear before all elements greater than x.
# X should be on right partition.
#
# Like, if linked list is:
# 3->5->8->5->10->2->1 and x = 5
#
# Resultant linked list should be:
# 3->2->1->5->8->5->10
#
# Approach:
# Maintain 2 linked list 'BEFORE' and 'AFTER'. Traverse given linked list, if
# value at current node is less than x insert this node at end of 'BEFORE'
# linked list otherwise at end of 'AFTER' linked list.
# At the end, merge both linked lists.
#
# Complexity:
# O(n)

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

  def partitionList(self, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    p = self.start
    present = 0
    while p is not None:
      if p.info == x:
        present = 1
      if p.info < x:
        if before_start is None:
          before_start = p
          before_end = p
        else:
          before_end.next = p
          before_end = before_end.next
      else:
        if after_start is None:
          after_start = p
          after_end = p
        else:
          after_end.next = p
          after_end = after_end.next
      p = p.next
    if not present:
      print('Element %d is not present in the list.' % x)
      return False

    # May be possible that given x is not in the list
    # so check for after_start for assigning the next to None
    after_end.next = None
    if before_end is None:
      self.start = after_start
      return True
    # merge both link lists
    before_end.next = after_start
    self.start = before_start
    return True

def main():
  print ('*************** LIST ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([3, 5, 8, 5, 10, 2, 1])
  link_list_1.traverse()
  print ('\n***** LIST AFTER PARTITIONS BY A NUMBER *****')
  if link_list_1.partitionList(5):
    link_list_1.traverse()

if __name__ == '__main__':
  main()