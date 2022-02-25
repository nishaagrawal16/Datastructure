# Date: 13-Dec-2019
# Vertical order traversal of a Binary Tree
# https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/#
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#           \  /\
#           8 10 9
#              \
#              11
#               \
#                12
# O(n)
# Efficient solution

import collections

class Node:
  def __init__(self, value):
    self.info = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

  def verticalOrderTraversal(self, root):
    if root is None:
      return

    m = {}
    hd = 0
    q = collections.deque([(root, hd)])

    while len(q):
      root, hd = q.popleft()

      # Check hd is not present in dictionary, create a list
      # as value corresponding to hd as key.
      if hd not in m:
        m[hd] = []
      m[hd].append(root.info)

      if root.left:
        q.append((root.left, hd - 1))

      if root.right:
        q.append((root.right, hd + 1))

    for key in sorted(m):
      for i in m[key]:
        print(i, end=' ')
      print('')


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)
  root.right.left.right =Node(8)
  root.right.right.left = Node(10)
  root.right.right.right = Node(9)
  root.right.right.left.right = Node(11)
  root.right.right.left.right.right = Node(12)
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(root)
  print('\n******* VERTICAL ORDER TRAVERSAL ********')
  t.verticalOrderTraversal(root)


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 4 2 5 1 6 8 3 10 11 12 7 9
# ******* VERTICAL ORDER TRAVERSAL ********
# 4
# 2
# 1 5 6
# 3 8 10
# 7 11
# 9 12
