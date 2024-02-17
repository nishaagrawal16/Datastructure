"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Complexity
----------
O(n)
"""

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

class Solution:
  def swapPairs(self, head):
    if head is None:
      return None
    if head.next is None:
      return head
    p = head
    q = None
    newHead = None
    traverse = 0
    prev = None
    while p is not None and p.next is not None:
      q = p.next
      p.next = q.next
      q.next = p
      traverse += 1
      if traverse == 1:
        newHead = q
      else:
        prev.next = q
      prev = p
      p = p.next
      q = None
    return newHead

def main():
  print ('*************** LIST ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([1,2, 3, 4])
  link_list_1.traverse()
  s = Solution()
  output = s.swapPairs(link_list_1.start)
  link_list_1.start = output
  print('**************** SWAPED LIST ***************')
  link_list_1.traverse()


if __name__ == '__main__':
  main()

# Output
# -------
# *************** LIST ***********************
# 1 ->2 ->3 ->4 ->None
# **************** SWAPED LIST ***************
# 2 ->1 ->4 ->3 ->None
