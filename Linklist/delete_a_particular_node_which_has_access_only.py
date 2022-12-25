#!/usr/bin/python

# Date: 2019-06-24
#
# Description:
# Delete a node of a singly linked list, given only access to that node.
#
# Approach:
# As we don't have access to head, we can't go back or so. We can copy the data
# from next node to this and delete the next node.
#
# Note: If reference to last node is given then we can't follow this approach.
#
# Complexity:
# O(1)

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
      print('%d ->' % p.info, end='')
      p = p.next
    print ('None')

  def delete_a_particular_node(self, node):
    next_node = node.next
    node.info = next_node.info
    node.next = next_node.next

def main():
  print ('*************** LIST ***********************')
  link_list = LinkList()
  link_list.create_list([1, 3, 5, 10, 20, 30])
  link_list.traverse()
  print('*************** AFTER REMOVING 5 ************')
  link_list.delete_a_particular_node(link_list.start.next.next)
  link_list.traverse()


if __name__ == '__main__':
  main()
