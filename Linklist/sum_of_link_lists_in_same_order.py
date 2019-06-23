#!/usr/bin/python

# Date: 2019-06-23
#
# Description:
# Two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in forward order, such that the 1's digit is at
# the tail of the list. Write a function that adds the two numbers and returns
# the sum as a linked list in forward order. For example:
#
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
# Output: 9 -> 1 -> 2. That is, 912.
# 
#
# Approach:
# Add padding 0's at starting of list which is shorter. Use recursive approach
# to reach at end of each list, keep adding corresponding digits and track
# carry also.
# If sum of most significant digits also return a carry then handle this also,
# insert 1 to start of list again.
#
# Complexity:
# O(n), where n = length of larger list.

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

  def length(self):
    p = self.start
    count = 0
    while p is not None:
      count += 1
      p = p.next
    return count

  def adding_zeros(self, count):
    i = 0
    while i < count:
      temp = Node(0)
      temp.next = self.start
      self.start = temp
      i += 1

  def add_node_at_start(self, value):
    node = Node(value)
    node.next = self.start
    self.start = node

  def sum_of_linklist_rec(self, node_1, node_2):
    if node_1 is None and node_2 is None:
      return 0

    carry = self.sum_of_linklist_rec(node_1.next, node_2.next)
    value = carry + node_1.info + node_2.info
    self.add_node_at_start(value%10)
    
    # Returning carry i.e if value = 18, carry=18/10
    return value/10    

  def sum_of_linklist_in_same_order(self, l1, l2):
    len_l1 = l1.length()
    len_l2 = l2.length()
    if len_l1 > len_l2:
      l2.adding_zeros(len_l1 - len_l2)
    elif len_l1 < len_l2:
      l1.adding_zeros(len_l2 - len_l1)
    if self.sum_of_linklist_rec(l1.start, l2.start):
      self.add_node_at_start(1)

def main():
  print ('*************** LIST-1 ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([7, 1, 6])
  link_list_1.traverse()
  print ('*************** LIST-2 ***********************')
  link_list_2 = LinkList()
  link_list_2.create_list([5, 9, 2])
  link_list_2.traverse()
  print('********* SUM OF LINKLIST IN REVERSE *********')
  link_list_result = LinkList()
  link_list_result.sum_of_linklist_in_same_order(link_list_1, link_list_2)
  link_list_result.traverse()

if __name__ == '__main__':
  main()

# Output
# ------
# *************** LIST-1 ***********************
# 7 ->  1 ->  6 ->  None
# *************** LIST-2 ***********************
# 5 ->  9 ->  2 ->  None
# ********* SUM OF LINKLIST IN REVERSE *********
# 1 ->  3 ->  0 -> 6 ->  None
