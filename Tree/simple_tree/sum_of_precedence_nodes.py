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

  def treeTraversalPostOrder(self, root):
    if root:
      precedence_sum = 0
      self.treeTraversalPostOrder(root.left)
      self.treeTraversalPostOrder(root.right)
      print root.data,
      if root.left:
        precedence_sum = precedence_sum + root.left.data
      if root.right:
        precedence_sum = precedence_sum + root.right.data
      if precedence_sum:
        root.data = precedence_sum
      print "Sum of nodes precedence: ", root.data

  def sumOfPrecedenceWithOutRecursion(self, root):
    if root is None:
      return
    s = []
    s.append(root)
    while True:
      if root.left:
        s.append(root.left)
        root = root.left
      elif s:
        precedence_sum = 0      
        root = s.pop()
        if root.left:
          precedence_sum = precedence_sum + root.left.data
        if root.right:
          precedence_sum = precedence_sum + root.right.data
        if precedence_sum:
          root.data = precedence_sum
        print "Sum of nodes precedence: ", root.data
      else:
        break          


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  t.treeTraversalPostOrder(t.root)
  

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
