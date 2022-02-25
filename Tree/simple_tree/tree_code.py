#         10
#       /   \
#      20   30
#     / \
#    40 50
# O(n)

import collections

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
      print(root.info, end=' ')
      self.treeTraversaPreOrder(root.left)
      self.treeTraversaPreOrder(root.right)

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

  def treeTraversalPostOrder(self, root):
    if root:
      self.treeTraversalPostOrder(root.left)
      self.treeTraversalPostOrder(root.right)
      print(root.info, end=' ')

  # Description:
  # Level order traversal of tree.
  #
  # Approach:
  # Uses DFS traversal approach.
  # 1. Prints current node info.
  # 2. enqueue's both left and right child.
  # 3. dequeue a node from queue.
  # 4. Execute while queue is not empty.
  #
  # Reference:
  # https://www.geeksforgeeks.org/?p=2686
  #
  # Complexity:
  # O(n), n is number of node in tree. Requires extra space to maintain queue.
  #/
  def levelOrderTraversal(self, root):
    if root is None:
      return
    q = collections.deque([root])

    while len(q):
      root = q.popleft()
      print(root.info, end=' ')
      if root.left:
        q.append(root.left)
      if root.right:
        q.append(root.right)

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** PREORDER TRAVERSAL ***********')
  t.treeTraversaPreOrder(t.root)
  print('\n********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n********** POSTORDER TRAVERSAL **********')
  t.treeTraversalPostOrder(t.root)
  print('\n********* LEVEL ORDER TRAVERSAL **********')
  t.levelOrderTraversal(t.root)
  print('')


if __name__ == '__main__':
  main()


# Output:
# ------
# ***************** TREE ******************

# ********** PREORDER TRAVERSAL ***********
# 10 20 40 50 30
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ********** POSTORDER TRAVERSAL **********
# 40 50 20 30 10
# ********* LEVEL ORDER TRAVERSAL **********
# 10 20 30 40 50
