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

  def treeTraversaPreOrder(self, root):
    if root:
      print(root.info)
      self.treeTraversaPreOrder(root.left)
      self.treeTraversaPreOrder(root.right)

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info)
      self.treeTraversalInOrder(root.right)

  def treeTraversalPostOrder(self, root):
    if root:
      self.treeTraversalPostOrder(root.left)
      self.treeTraversalPostOrder(root.right)
      print(root.info)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** PREORDER TRAVERSAL ***********')
  t.treeTraversaPreOrder(t.root)
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('********** POSTORDER TRAVERSAL **********')
  t.treeTraversalPostOrder(t.root)


if __name__ == '__main__':
  main()