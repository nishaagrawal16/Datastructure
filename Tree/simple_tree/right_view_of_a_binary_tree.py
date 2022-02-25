# Print Right View of a Binary Tree (Last node of every levels)
# https://www.geeksforgeeks.org/print-right-view-binary-tree-2/
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

  def viewRight(self, root):
    max_level = [0]
    self.viewRightUtil(root, 1, max_level)

  def viewRightUtil(self, root, level, max_level):
    if root is None:
      return

    if max_level[0] < level:
      print(root.info, end=' ')
      max_level[0] = level

    self.viewRightUtil(root.right, level + 1, max_level)
    self.viewRightUtil(root.left, level + 1, max_level)

  def viewRightThroughIteration(self, root):
    if root is None:
      return

    hd = 0
    q = collections.deque([(root, hd)])

    while len(q):
      n = len(q)

      # This is for checking to all level.
      for i in range(n):
        root, hd = q.popleft()
        # For printing the last node of every level for right view.
        if i + 1 == n:
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
  print('\n************* RIGHT VIEW ***************')
  t.viewRight(t.root)
  print('\n************* RIGHT VIEW THROUGH ITERATION ***************')
  t.viewRightThroughIteration(t.root)
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
# ************* RIGHT VIEW ***************
# 10 30 50
