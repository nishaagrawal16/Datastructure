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

class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None
    self.hd = 0

class Tree:
  def __init__(self):
    self.root = None

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print root.data,
      self.treeTraversalInOrder(root.right)

  def verticalOrderTraversal(self, root):
    if root is None:
      return

    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)

    while len(q):
      root = q.pop(0)
      hd = root.hd

      # Check hd is not present in dictionary, create a list
      # as value corresponding to hd as key.
      if hd not in m:
        m[hd] = []
      m[hd].append(root.data)

      if root.left:
        root.left.hd = hd - 1
        q.append(root.left)

      if root.right:
        root.right.hd = hd + 1
        q.append(root.right)

    for key in sorted(m):
      for i in m[key]:
        print i,
      print
      

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
