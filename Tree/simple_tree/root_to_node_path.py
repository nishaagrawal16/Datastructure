"""
Print root to Node path
https://www.youtube.com/watch?v=fmflMqVOC7k
        1
       / \
      2   3
     / \
    4   5
       / \
      6   7
Complexity
----------
Time: O(n)
Space: O(n)
"""

from collections import deque

class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def createTree(self):
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    self.root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n6
    n5.right = n7

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.val, end=' ')
      self.treeTraversalInOrder(root.right)

class Solution:
  def findPath(self, root, arr, val):
    if root is None:
      return False
    arr.append(root.val)
    if root.val == val:
      return True
    left_status = self.findPath(root.left, arr, val)
    right_status = self.findPath(root.right, arr, val)
    if left_status is False and right_status is False:
      arr.pop(-1)
      return False
    return True


def main():
  print('******************** Tree **********************')
  t = Tree()
  t.createTree()
  print('************* INORDER TRAVERSAL ****************')
  t.treeTraversalInOrder(t.root)
  s = Solution()
  arr = []
  print('\n********* Path from root: 1 to node: 7 *********')
  Output = s.findPath(t.root, arr, 7)
  print('Path:', arr)


if __name__ == '__main__':
  main()

# Output:
#---------
# ******************** Tree **********************
# ************* INORDER TRAVERSAL ****************
# 4 2 6 5 7 1 3
# ********* Path from root: 1 to node: 7 *********
# Path: [1, 2, 5, 7]
