#!/usr/bin/python

# Date: 2018-09-18
#
# Description:
# Two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at
# the head of the list. Write a function that adds the two numbers and returns
# the sum as a linked list. Example:
#
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
# Output: 2 -> 1 -> 9. That is, 912
#
# Approach:
# As numbers are stored in reverse order we can scan the two linked lists and
# add corresponding digits to end of another list. If there is carry we have to
# take care of that in next digits that will be added.
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

def sum_of_reverse_linklist(l1, l2):
  p1 = l1.start
  p2 = l2.start
  l3 = LinkList()
  carry = 0
  while p1 is not None or p2 is not None or carry:
    s = carry
    if p1:
      s += p1.info
      p1 = p1.next
    if p2:
      s += p2.info
      p2 = p2.next    
    if s >= 10:
      carry = 1
    else:
      carry = 0
    temp = Node(s%10)
    if l3.start is None:
      l3.start = temp
      p3 = l3.start
    else:
      p3.next = temp
      p3 = p3.next

  print('********* SUM OF LINKLIST IN REVERSE *********')
  l3.traverse()   
  
def main():
  print ('*************** LIST-1 ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([7, 1, 6])
  link_list_1.traverse()
  print ('*************** LIST-2 ***********************')
  link_list_2 = LinkList()
  link_list_2.create_list([5, 9, 2])
  link_list_2.traverse()
  sum_of_reverse_linklist(link_list_1, link_list_2)

if __name__ == '__main__':
  main()

# Output
# ------
# *************** LIST-1 ***********************
# 7 ->  1 ->  6 ->  None
# *************** LIST-2 ***********************
# 5 ->  9 ->  2 ->  None
# ********* SUM OF LINKLIST IN REVERSE *********
# 2 ->  1 ->  9 ->  None