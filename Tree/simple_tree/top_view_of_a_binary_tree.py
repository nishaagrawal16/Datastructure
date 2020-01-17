# Date: 13-Dec-2019
# Print Top View of a Binary Tree (First node of every Vertical levels)
# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/#
#         10
#       /   \
#      20   30
#     / \     
#    40 50     
# O(n)

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

  def viewTop(self, root):
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
      # Check hd is present in dictionary otherwise add it.
      if hd not in m:
        m[hd] = root.data

      if root.left:
        root.left.hd = hd - 1
        q.append(root.left)

      if root.right:
        root.right.hd = hd + 1
        q.append(root.right)
    
    for key in sorted(m):
      print m[key],


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* TOP VIEW ****************')
  t.viewTop(t.root)
  

if __name__ == '__main__':
  main()


# Output:
# -------
# 
# ***************** TREE ******************
# 
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30 
# ************* TOP VIEW ****************
# 40 20 10 30
