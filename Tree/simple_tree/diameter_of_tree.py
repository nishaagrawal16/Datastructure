# Date: 01-03-2022
#
# Description:
# Find diameter(or max width) of a tree. The diameter of a tree is the number of
# nodes on the longest path between two leaves in the tree.
#
# Approach:
# Diameter of a tree can be calculated by only using the height function,
# because the diameter of a tree is nothing but maximum value of (left_height + right_height + 1)
# for each node. So we need to calculate this value (left_height + right_height + 1)
# for each node and update the result.
#
# Reference:
# https://www.geeksforgeeks.org/diameter-of-a-binary-tree-in-on-a-new-method/
#
#         10
#       /   \
#      20   30
#     / \
#    40 50
# O(n)

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

def height(node, d):
  if node is None:
    return 0
  else:
    left_height = height(node.left, d)
    right_height = height(node.right, d)
    d[0] = max(d[0], (left_height + left_height + 1))
    return 1 + max(left_height, right_height)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* TREE DIAMETER ***************')
  d = [0]
  h = height(t.root, d)
  print('DIAMETER: ', d[0])


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ************* TREE DIAMETER ***************
# DIAMETER:  5
