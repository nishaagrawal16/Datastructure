
# Date: 21-Nov-2019
# Description:
# - Insert in Binary search tree(BST)
# - Search in BST
# - Delete from BST
# Reference:
# http://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# http://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# Complexity:
# Insert, search, delete - O(logn) in avarage case(Balanced binary tree)
# otherwise in worst case O(n) (Not balanced tree means only has left child or right child)
# Traversal - O(n)
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

class Node:
  def __init__(self, value):
    self.info = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, root, key):
    if root is None:
      return Node(key)
    else:
      if key == root.info:
        return root
      elif key < root.info:
        root.left = self.insert(root.left, key)
      else:
        root.right = self.insert(root.right, key)
    return root

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

  def search(self, root, val):
    if root is None or root.info == val:
      return root
    if val < root.info:
      return self.search(root.left, val)
    return self.search(root.right, val)

  def delete(self, root, val):
    if root is None:
      return root

    if val < root.info:
      root.left = self.delete(root.left, val)
    elif val > root.info:
      root.right = self.delete(root.right, val)
    else:
      # root has only one child or no child
      if root.left is None:
        temp = root.right
        root = None
        return temp

      if root.right is None:
        temp = root.left
        root = None
        return temp

      # Node with two children: Get the inorder successor
      # (smallest in the right subtree)
      temp = self.minValueNode(root.right)

      root.info = temp.info

      root.right = self.delete(root.right, temp.info)
    return root


  def minValueNode(self, root):
    current = root
    while current.left is not None:
      current = current.left

    return current

def main():
  print('*****************BINARY TREE ************\n')
  t = Tree()
  t.root = Node(50)
  t.root = t.insert(t.root, 30)
  t.root = t.insert(t.root, 20)
  t.root = t.insert(t.root, 40)
  t.root = t.insert(t.root, 70)
  t.root = t.insert(t.root, 60)
  t.root = t.insert(t.root, 80)
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************** SEARCHING ****************')
  if t.search(t.root, 60):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************** DELETION 20 ***************')
  t.delete(t.root, 20)
  print('********** INORDER TRAVERSAL *************')
  t.treeTraversalInOrder(t.root)
  print('\n************** SEARCHING *****************')
  if t.search(t.root, 30):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************** DELETION 30****************')
  t.delete(t.root, 30)
  print('********** INORDER TRAVERSAL *************')
  t.treeTraversalInOrder(t.root)
  print('\n************** DELETION 50****************')
  t.delete(t.root, 50)
  print('********** INORDER TRAVERSAL *************')
  t.treeTraversalInOrder(t.root)
  print('')


if __name__ == '__main__':
  main()

# Output:
# ------
# *****************BINARY TREE ************
#
# ********** INORDER TRAVERSAL ************
# 20 30 40 50 60 70 80
# ************** SEARCHING ****************
# value found
# ************** DELETION 20 ***************
# ********** INORDER TRAVERSAL *************
# 30 40 50 60 70 80
# ************** SEARCHING *****************
# value found
# ************** DELETION 30****************
# ********** INORDER TRAVERSAL *************
# 40 50 60 70 80
# ************** DELETION 50****************
# ********** INORDER TRAVERSAL *************
# 40 60 70 80
