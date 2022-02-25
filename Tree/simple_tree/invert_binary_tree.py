# Invert binary tree
# https://leetcode.com/problems/invert-binary-tree/
#
#         10
#       /   \
#      20   30
#     / \
#    40 50
# O(n)

import collections

class Node:
  def __init__(self, value):
    self.info = value
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
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

  def invertTree(self, root):
    if root is None:
      return root

    q = collections.deque([root])
    while q:
      data = q.popleft()
      data.left, data.right = data.right, data.left
      if data.left:
        q.append(data.left)
      if data.right:
        q.append(data.right)
    return root

  # Through Recursion:
  # ------------------
  # def invertTree(self, root):
  #   if root is None:
  #     return root

  #   root.left, root.right = root.right, root.left
  #   root.left = self.invertTree(root.left)
  #   root.right = self.invertTree(root.right)
  #   return root

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  invertedTreeRoot = t.invertTree(t.root)
  print('\n********** INORDER TRAVERSAL OF INVERTED TREE ************')
  t.treeTraversalInOrder(invertedTreeRoot)
  print('')

if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ********** INORDER TRAVERSAL OF INVERTED TREE ************
# 30 10 50 20 40
