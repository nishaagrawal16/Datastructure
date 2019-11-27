 
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
# Limitation:
# If BST is not balanced (or skwed trees), it becomes a linked list and all
# operations take O(n) complexity. This problem is handled by balancing trees.
# AVL, Red-black, B trees are examples of balanced trees.

class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, root, node):
    if root is None:
      root = node
      return
    
    if node.data < root.data:
      if root.left is None:
        root.left = node
      else:
        self.insert(root.left, node)
    else:
      if root.right is None:
        root.right = node
      else:
        self.insert(root.right, node)
      
  def treeTraversalInOrder(self, root):    
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.data)
      self.treeTraversalInOrder(root.right)

  def search(self, root, val):
    if root is None or root.data == val:
      return root
    if val < root.data:
      return self.search(root.left, val)
    return self.search(root.right, val)

  def delete(self, root, val):
    if root is None:
      return root

    if val < root.data:
      root.left = self.delete(root.left, val)
    elif val > root.data:
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

      root.data = temp.data

      root.right = self.delete(root.right, temp.data)
    return root


  def minValueNode(self, root):
    current = root
    while current.left is not None:
      current = current.left

    return current
    
def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.root = Node(50)
  t.insert(t.root, Node(30))
  t.insert(t.root, Node(20))
  t.insert(t.root, Node(40))
  t.insert(t.root, Node(70))
  t.insert(t.root, Node(60))
  t.insert(t.root, Node(80))
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('************** SEARCHING ****************')
  if t.search(t.root, 60):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************** DELETION 20 ***************')
  t.delete(t.root, 20)
  print('********** INORDER TRAVERSAL *************')
  t.treeTraversalInOrder(t.root)
  print('************** SEARCHING *****************')
  if t.search(t.root, 30):
    print('value found')
  else:
    print('value is not present in the tree')
  print('************** DELETION 30****************')
  t.delete(t.root, 30)
  print('********** INORDER TRAVERSAL *************')
  t.treeTraversalInOrder(t.root)
  print('************** DELETION 50****************')
  t.delete(t.root, 50)
  print('********** INORDER TRAVERSAL *************')
  t.treeTraversalInOrder(t.root)


if __name__ == '__main__':
  main()

# Output:
# ------
# ********** INORDER TRAVERSAL ************
# 20
# 30
# 40
# 50
# 60
# 70
# 80
