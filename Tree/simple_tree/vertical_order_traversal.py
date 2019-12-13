# Date: 13-Dec-2019
# Vertical order traversal of a Binary Tree
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
#         10
#       /   \
#      20   30
#     / \     
#    40 50     
# 
# min --> Minimum horizontal distance from root
# max --> Maximum horizontal distance from root
# hd  --> Horizontal distance of current node from root
# O(m*n)
# Where m is th elength of min to max (range)
# n is the number of nodes of tree


class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None
    self.hd = 0

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
      print root.data,
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
    print root.data, 

  verticalOrderTraversal(root.left, line_no, hd - 1)
  verticalOrderTraversal(root.right, line_no, hd + 1)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n***** VERTICAL ORDER TRAVERSAL*********')
  min = [0]
  max = [0]
  hd = 0
  minMaxOfTree(t.root, min, max, hd)
  for line_no in range(min[0], max[0] + 1):
    verticalOrderTraversal(t.root, line_no, hd)
    print


if __name__ == '__main__':
  main()


# Output:
# -------
# 
# ***************** TREE ******************
# 
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30 
# ***** VERTICAL ORDER TRAVERSAL*********
# 40
# 20
# 10 50
# 30
