"""
https://leetcode.com/problems/add-two-numbers/

Complexity
----------
O(max(m, n)) time and space
"""

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
    l3 = ListNode(-1)
    p = l3
    carry = 0
    while l1 or l2 or carry:
      val = 0
      if l1:
        val += l1.val
        l1 = l1.next
      if l2:
        val += l2.val
        l2 = l2.next
      if carry:
        val += carry
      p.next = ListNode(val % 10)
      p = p.next
      carry = val // 10
    return l3.next

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

# Output:
#---------
# ********** LIST-1 ***************
# 7 -> 1 -> 6 -> None
# ********** LIST-2 ***************
# 5 -> 9 -> 2 -> None
# ********** SUM OF LINKLIST IN REVERSE ***************
# 2 -> 1 -> 9 -> None
