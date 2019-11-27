class Node:
  def __init__(self, value):
    self.info = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None
    self.count = 0

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

  def treeTraversaPreOrder(self, root):
    if root:
      print(root.info)
      self.treeTraversaPreOrder(root.left)
      self.treeTraversaPreOrder(root.right)

  def NthNodeOfPreOrderTraversal(self, root, n):
    if root:
      self.count = self.count + 1
      if self.count == n:
        print(root.info)
      self.NthNodeOfPreOrderTraversal(root.left, n)
      self.NthNodeOfPreOrderTraversal(root.right, n)
       
  def treeTraversalInOrder(self, root):    
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info)
      self.treeTraversalInOrder(root.right)

  def NthNodeOfInOrderTraversal(self, root, n):
    if root:
      self.NthNodeOfInOrderTraversal(root.left, n)
      self.count = self.count + 1
      if self.count == n:
        print(root.info)
      self.NthNodeOfInOrderTraversal(root.right, n)

  def treeTraversalPostOrder(self, root):
    if root:
      self.treeTraversalPostOrder(root.left)
      self.treeTraversalPostOrder(root.right)
      print(root.info)

  def NthNodeOfPostOrderTraversal(self, root, n):
    if root:
      self.NthNodeOfPostOrderTraversal(root.left, n)
      self.NthNodeOfPostOrderTraversal(root.right, n)
      self.count = self.count + 1
      if self.count == n:
        print(root.info)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** PREORDER TRAVERSAL ***********')
  t.treeTraversaPreOrder(t.root)

  print('********** PREORDER TRAVERSAL Nth ************')
  t.NthNodeOfPreOrderTraversal(t.root, 3)

  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  t.count = 0
  print('********** INORDER TRAVERSAL Nth ************')
  t.NthNodeOfInOrderTraversal(t.root, 3)

  print('********** POSTORDER TRAVERSAL **********')
  t.treeTraversalPostOrder(t.root)
  t.count = 0
  print('********** POSTORDER TRAVERSAL Nth ************')
  t.NthNodeOfPostOrderTraversal(t.root, 3)

if __name__ == '__main__':
  main()