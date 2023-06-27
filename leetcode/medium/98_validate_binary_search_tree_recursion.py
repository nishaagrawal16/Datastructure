"""
https://leetcode.com/problems/validate-binary-search-tree/
#         10
#       /   \
#      20   30
#     / \
#    40 50
Complexity
----------
O(n)
"""
import math

class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def createTree(self):
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    self.root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.val, end=' ')
      self.treeTraversalInOrder(root.right)

class Solution:
  def isValidBST(self, root):
    if root is None:
      return True
    return self.isValidBSTUtils(root, -math.inf, math.inf)

  def isValidBSTUtils(self, root, _min, _max):
    if root is None:
      return True
    if root.val <= _min or root.val >= _max:
      return False
    return self.isValidBSTUtils(root.left, _min, root.val) and self.isValidBSTUtils(root.right, root.val, _max)


def main():
  print('***************** TREE ******************')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  s = Solution()
  output = s.isValidBST(t.root)
  if output:
    print('\nGiven tree is Binary search Tree')
  else:
    print('\nGiven tree is not the Binary search Tree')


if __name__ == '__main__':
  main()

# Output:
#---------
# ***************** TREE ******************
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# Given tree is not the Binary search Tree
