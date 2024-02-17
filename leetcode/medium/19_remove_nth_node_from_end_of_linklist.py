"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
  def removeNthFromEnd(self, head, n):
    if head is None:
      return None
    count = self.countNodes(head)
    travelNodes = count - n
    p = head
    if travelNodes == 0:
      return p.next
    i = 1
    while p is not None and i < travelNodes:
      p = p.next
      i += 1
    p.next = p.next.next
    return head

  def countNodes(self, head):
    count = 0
    p = head
    while p is not None:
        p = p.next
        count += 1
    return count

def main():
  print ('*************** LIST ***********************')
  link_list_1 = LinkList()
  link_list_1.create_list([1,2, 3, 4, 5])
  link_list_1.traverse()
  s = Solution()
  output = s.removeNthFromEnd(link_list_1.start, 2)
  link_list_1.start = output
  print('After removal of 2nd node from the last')
  link_list_1.traverse()


if __name__ == '__main__':
  main()

# Output
# -------
# *************** LIST ***********************
# 1 ->2 ->3 ->4 ->5 ->None
# After removal of 2nd node from the last
# 1 ->2 ->3 ->5 ->None
