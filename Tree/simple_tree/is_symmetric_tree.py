# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#         10
#       /    \
#      20    20
#     / \    / \
#    30  40 40  30
# O(n)

import collections

class Node:
  def __init__(self, infoue):
    self.info = infoue
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def createTree(self):
    n1 = Node(10)
    n12 = Node(20)
    n13 = Node(30)
    n14 = Node(40)
    n22 = Node(20)
    n23 = Node(40)
    n24 = Node(30)
    self.root = n1
    n1.left = n12
    n1.right = n22
    n12.left = n13
    n12.right = n14
    n22.left = n23
    n22.right = n24

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

  def isSymmetric(self, root):
    if root is None:
      return True

    return self.isSymmetricUtils(root.left, root.right)

  def isSymmetricUtils(self, left, right):
    if left is None:
      return left == right

    if left and right and left.info == right.info:
      return (self.isSymmetricUtils(left.left, right.right) and \
        self.isSymmetricUtils(left.right, right.left))
    return False

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\nTree is symmetric: ', t.isSymmetric(t.root))

if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 30 20 40 10 40 20 30
# Tree is symmetric:  True

