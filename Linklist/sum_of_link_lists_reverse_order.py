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

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class LinkList:
  def __init__(self):
    self.start = None

  def create_list(self, li):
    if self.start is None:
      self.start = ListNode(li[0])
    p = self.start
    for i in range(1,len(li)):
      temp = ListNode(li[i])
      p.next = temp
      p = p.next

  def traverse(self):
    p = self.start
    while p is not None:
      print('%d -> ' % p.val, end='')
      p = p.next
    print('None')

class Solution:
  def addTwoNumbers(self, l1, l2):
    p1 = l1
    p2 = l2
    start3 = None
    carry = 0
    while p1 is not None or p2 is not None:
      sum = 0
      if p1 is not None:
        sum = sum + p1.val
        p1 = p1.next
      if p2 is not None:
        sum = sum + p2.val
        p2 = p2.next
      sum = sum + carry
      rem = sum % 10
      carry = sum // 10
      node = ListNode(rem)
      if start3 is None:
        start3 = node
        l3 = start3
      else:
        l3.next = node
        l3 = l3.next
    if carry:
      l3.next = ListNode(carry)

    return start3
def main():
  print('********** LIST-1 ***************')
  link_list_1 = LinkList()
  link_list_1.create_list([7, 1, 6])
  link_list_1.traverse()
  print('********** LIST-2 ***************')
  link_list_2 = LinkList()
  link_list_2.create_list([5, 9, 2])
  link_list_2.traverse()
  s = Solution()
  print('********** SUM OF LINKLIST IN REVERSE ***************')
  start3 = s.addTwoNumbers(link_list_1.start, link_list_2.start)
  list3 = start3
  while list3 is not None:
    print('%d -> ' % list3.val, end='')
    list3 = list3.next
  print('None')


if __name__ == '__main__':
  main()
