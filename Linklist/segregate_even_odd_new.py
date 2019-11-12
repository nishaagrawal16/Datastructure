#!/usr/bin/python

# Date: 2018-09-17
#
# Description:
# There is a linked list given and a value x, segregate a linked list in even odd elements
# that all element should be appear as below output
#
# Like, if linked list is:
# 17 ->  15 ->  8 ->  12 ->  10 ->  5 ->  4 ->  1 ->  7 ->  6 ->  None
#
# Resultant linked list should be:
# 8 ->  12 ->  10 ->  4 ->  6 ->  17 ->  15 ->  5 ->  1 ->  7 ->  None
#
# Approach:
# Maintain 2 linked list 'BEFORE' and 'AFTER'. Traverse given linked list, if
# value at current node is even then insert this node at end of 'BEFORE'
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

  def prepareEvenOdd(self):
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    p = self.start
    while p is not None:
      print('p.info:', p.info)
      if p.info %2 == 0:
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
    if after_end:
      after_end.next = None
    if before_end is None:
      self.start = after_start
    else:
    # merge both link lists
      before_end.next = after_start
      self.start = before_start

def main():
  print ('*************** LIST ***********************')
  link_list = LinkList()
  link_list.create_list([17, 15, 8, 12, 10, 5, 4, 1, 7, 6])
  # link_list.create_list([8, 12, 10, 5, 4, 1,6])
  # link_list.create_list([8, 12, 10])
  # link_list.create_list([1, 3, 5, 7])
  link_list.traverse()
  print ('\n***** LIST AFTER PARTITIONS BY A NUMBER *****')
  link_list.prepareEvenOdd()
  link_list.traverse()


if __name__ == '__main__':
  main()