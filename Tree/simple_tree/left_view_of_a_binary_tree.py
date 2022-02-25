# Print Left View of a Binary Tree (First node of every levels)
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
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

  def viewLeft(self, root):
    max_level = [0]
    self.viewLeftUtil(root, 1, max_level)

  def viewLeftUtil(self, root, level, max_level):
    if root is None:
      return

    if max_level[0] < level:
      print(root.info, end=' ')
      max_level[0] = level

    self.viewLeftUtil(root.left, level + 1, max_level)
    self.viewLeftUtil(root.right, level + 1, max_level)

  def viewLeftThroughIteration(self, root):
    if root is None:
      return

    hd = 0
    q = collections.deque([(root, hd)])

    while len(q):
      n = len(q)

      # This is for checking to all level.
      for i in range(n):
        root, hd = q.popleft()
        # For printing the first node of every level as left view.
        if i == 0:
          print(root.info, end=' ')

        if root.left:
          q.append((root.left, hd - 1))

        if root.right:
          q.append((root.right, hd + 1))


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* Left VIEW ***************')
  t.viewLeft(t.root)
  print('\n************* Left VIEW THROUGH ITERATION ***************')
  t.viewLeftThroughIteration(t.root)
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
# ************* Left VIEW ***************
# 10 20 40
