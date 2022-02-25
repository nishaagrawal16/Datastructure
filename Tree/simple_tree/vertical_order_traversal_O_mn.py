# Date: 13-Dec-2019
# Vertical order traversal of a Binary Tree
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
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
#
# min --> Minimum horizontal distance from root
# max --> Maximum horizontal distance from root
# hd  --> Horizontal distance of current node from root
# O(m*n)
# Where m is the length of min to max (range)
# n is the number of nodes of tree
# Note: For long tree 12 print before 9 (Not very efficient solution)

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

def minMaxOfTree(root, min, max, hd):
  if root is None:
    return
  if hd < min[0]:
    min[0] = hd
  elif hd > max[0]:
    max[0] = hd
  minMaxOfTree(root.left, min, max, hd - 1)
  minMaxOfTree(root.right, min, max, hd + 1)
  # print min, max

def verticalOrderTraversal(root, line_no, hd):
  if root is None:
    return

  if line_no == hd:
    print(root.info, end=' ')

  verticalOrderTraversal(root.left, line_no, hd - 1)
  verticalOrderTraversal(root.right, line_no, hd + 1)


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
  print('\n***** VERTICAL ORDER TRAVERSAL*********')
  min = [0]
  max = [0]
  hd = 0
  minMaxOfTree(root, min, max, hd)
  for line_no in range(min[0], max[0] + 1):
    verticalOrderTraversal(root, line_no, hd)
    print('')


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 4 2 5 1 6 8 3 10 11 12 7 9
# ***** VERTICAL ORDER TRAVERSAL*********
# 4
# 2
# 1 5 6
# 3 8 10
# 7 11
# 12 9
