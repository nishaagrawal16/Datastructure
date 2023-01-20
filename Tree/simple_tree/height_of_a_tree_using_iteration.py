# Write a program to Calculate height of a tree | Iteration
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

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

# Computes height of a tree[Same as left view of a tree]
def height(root):
  if root is None:
    return 0

  q = collections.deque([root])
  height = 0
  while q:
    # process each node of the current level and enqueue their
    # non-empty left and right child
    for i in range(len(q)):
      root = q.popleft()

      if root.left:
        q.append(root.left)

      if root.right:
        q.append(root.right)

    # increment height by 1 for each level
    height += 1
  return height

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* TREE HEIGHT ***************')
  print(height(t.root))


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ************* TREE HEIGHT ***************
# 3
