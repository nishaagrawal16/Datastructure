# Date: 17-Dec-2019
# Print Bottom View of a Binary Tree (Last node of every Vertical levels)
# https://www.geeksforgeeks.org/bottom-view-binary-tree/
#
#        10
#       /  \
#      20  30
#     /  \
#    40  50
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

  def viewBottom(self, root):
    if root is None:
      return
    m = {}
    hd = 0
    q = collections.deque([(root, hd)])

    while len(q):
      root, hd = q.popleft()
      # Overwrite hd values with new value for getting the bottom view.
      m[hd] = root.info

      if root.left:
        q.append((root.left, hd - 1))

      if root.right:
        q.append((root.right, hd + 1))

    for key in sorted(m):
      print(m[key], end=' ')
    print('')


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* BOTTOM VIEW ***************')
  t.viewBottom(t.root)


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ************* BOTTOM VIEW ***************
# 40 20 50 30

