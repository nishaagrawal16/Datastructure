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
    print('TODO')

    
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
  print('************** DELETION ****************')
  t.delete(t.root, 20)


if __name__ == '__main__':
  main()