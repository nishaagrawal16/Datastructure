# Write a program to Calculate Size of a tree | Iteration
# Number of nodes
#         10
#       /   \
#      20   30
#     / \
#    40 50
# O(n)

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

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

# Computes the number of nodes in tree
def size(root):
  if root is None:
    return 0

  q = []
  count = 1
  q.append(root)
  while len(q):
    root = q.pop(0)
    if root.left:
      q.append(root.left)
      count = count + 1

    if root.right:
      q.append(root.right)
      count = count + 1

  return count


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* TREE SIZE ***************')
  print(size(t.root))


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ************* TREE SIZE ***************
# 5
