# 1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then 
#      a) Pop the top item from stack.
#      b) Print the popped item, set current = popped_item->right 
#      c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.

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

  def treeTraversalInOrder(self):
    current = self.root
    s = []
    while True:
      if current is not None:
        s.append(current)
        current = current.left
      elif s:
        current = s.pop()
        print current.data,
        current = current.right
      else:
        break


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder()


if __name__ == '__main__':
  main()