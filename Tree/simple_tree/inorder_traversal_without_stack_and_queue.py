# 1. Initialize current as root 
# 2. While current is not NULL
#    If the current does not have left child
#       a) Print current data
#       b) Go to the right, i.e., current = current->right
#    Else
#       a) Make current as the right child of the rightmost 
#          node in current's left subtree
#       b) Go to this left child, i.e., current = current->left

class Node:
  def __init__(self, value):
    self.data = value
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

  def MorrisTraversal(self, root):
    current = root
    while current is not None:
      if current.left is None:
        print current.data,
        current = current.right
      else:
        # Find the inorder predecessor of current 
        pre = current.left
        while(pre.right is not None and pre.right != current):
          pre = pre.right
        # Make current as right child of its inorder predecessor 
        if pre.right is None:
          pre.right = current
          current = current.left
        # Revert the changes made in if part to restore the  
        # original tree i.e., fix the right child of predecessor 
        else:
          pre.right = None
          print current.data,
          current = current.right


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.MorrisTraversal(t.root)


if __name__ == '__main__':
  main()