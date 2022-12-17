
# Date: 21-Nov-2019
# Description:
# - Insert in Binary search tree(BST)
# - Search in BST
# - Delete from BST
# Reference:
# Inorder Successor[O(logn)]: https://www.youtube.com/watch?v=5cPbNCrdotA&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=37
# http://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# http://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# Complexity:
# Insert, search, delete - O(logn) in avarage case(Balanced binary tree)
# otherwise in worst case O(n) (Not balanced tree means only has left child or right child)
# Traversal [O(n)]
# **Inorder traversal in binary serach tree will give so the sorted array.**
# Limitation:
# If BST is not balanced (or skwed trees), it becomes a linked list and all
# operations take O(n) complexity. This problem is handled by balancing trees.
# AVL, Red-black, B trees are examples of balanced trees.
#         50
#       /   \
#      30    70
#     / \    / \
#    20 40  60 80

import math

class TreesNode(object):
  def __init__(self, data) -> None:
    self.data = data
    self.left = None
    self.right = None

class Tree(object):
  def __init__(self):
    self.root = None

  def insert(self, root, data):
    if root == None:
      root = TreesNode(data)
    elif data <= root.data:
      root.left = self.insert(root.left, data)
    else:
      root.right = self.insert(root.right, data)
    return root

  def delete(self, root, val):
    if root is None:
      return root
    if val < root.data:
      root.left = self.delete(root.left, val)
    elif val > root.data:
      root.right = self.delete(root.right, val)
    else:
      # No child
      if root.left is None and root.right is None:
        return None
      # One child
      if root.left is None:
        temp = root.right
        root = None
        return temp

      if root.right is None:
        temp = root.left
        root = None
        return temp
      # Two children: Get the inorder successor
      # find smallest in the right subtree.
      temp = minValue(root.right)
      root.data = temp.data
      root.right = self.delete(root.right, temp.data)
    return root

  def InOrdertreeTraversal(self, root):
    if root == None:
      return
    self.InOrdertreeTraversal(root.left)
    print(root.data, end=' ')
    self.InOrdertreeTraversal(root.right)

  def search(self, root, val):
    if root is None or root.data == val:
      return root
    if val < root.data:
      return self.search(root.left, val)
    return self.search(root.right, val)

  def getSuccessor(self, root, val):
    if root is None:
      return root
    # Find the current.
    current = self.search(root, val)

    # Has right subtree
    if current.right is not None:
      # find min of right subtree
      return minValue(current)
    else:
      # Has no right subtree
      successor = None
      ancestor = root
      while current != ancestor:
        if current.data < ancestor.data:
          # So far this is the deepest node for which
          # current node is in left.
          successor = ancestor
          ancestor = ancestor.left
        else:
          ancestor = ancestor.right
      return successor

def minValue(root):
  current = root
  while current.left is not None:
    current = current.left
  return current

def checkBST(root, min_value, max_value):
  if root == None:
    return True
  if (root.data > min_value and root.data < max_value
      and checkBST(root.left, min_value, root.data) and
      checkBST(root.right, root.data, max_value)):
    return True
  else:
    return False

# O(n)
def checkBSTUtils(root):
  return checkBST(root, -math.inf, math.inf)


def main():
  print('*****************BINARY TREE ************')
  t = Tree()
  t.root = TreesNode(50)
  t.root = t.insert(t.root, 30)
  t.root = t.insert(t.root, 20)
  t.root = t.insert(t.root, 40)
  t.root = t.insert(t.root, 70)
  t.root = t.insert(t.root, 60)
  t.root = t.insert(t.root, 80)
  print('********** INORDER TRAVERSAL ************')
  t.InOrdertreeTraversal(t.root)
  print('\n** Check Tree is Binary Search tree ***')
  if checkBSTUtils(t.root):
    print('Yes')
  else:
    print('No')
  print('************ SEARCHING 60 ***************')
  if t.search(t.root, 60):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************ SEARCHING 10 ***************')
  if t.search(t.root, 10):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************* Successor of 60 ***********')
  successor = t.getSuccessor(t.root, 60)
  if successor:
    print(successor.data)
  print('************** DELETION 20 ***************')
  t.delete(t.root, 20)
  print('********** INORDER TRAVERSAL *************')
  t.InOrdertreeTraversal(t.root)
  print('\n************* SEARCHING 30 *************')
  if t.search(t.root, 30):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************** DELETION 30 ****************')
  t.delete(t.root, 30)
  print('********** INORDER TRAVERSAL **************')
  t.InOrdertreeTraversal(t.root)
  print('\n************** DELETION 50 **************')
  t.delete(t.root, 50)
  print('********** INORDER TRAVERSAL **************')
  t.InOrdertreeTraversal(t.root)
  print('')

if __name__ == '__main__':
  main()

# Output:
# ------
# *****************BINARY TREE ************
# ********** INORDER TRAVERSAL ************
# 20 30 40 50 60 70 80
# ** Check Tree is Binary Search tree ***
# Yes
# ************ SEARCHING 60 ***************
# value found
# ************ SEARCHING 10 ***************
# value is not present in the tree
# ************* Successor of 60 ***********
# 70
# ************** DELETION 20 ***************
# ********** INORDER TRAVERSAL *************
# 30 40 50 60 70 80
# ************* SEARCHING 30 *************
# value found
# ************** DELETION 30 ****************
# ********** INORDER TRAVERSAL **************
# 40 50 60 70 80
# ************** DELETION 50 **************
# ********** INORDER TRAVERSAL **************
# 40 60 70 80
