# Zig-Zag or Sprial Travesal
# https://www.youtube.com/watch?v=3OXWEdlIGl4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=20
#
#         10
#       /   \
#      20   30
#     / \
#    40 50
# Time Complexity: O(n)

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

def zigZagTraversal(node):
  if node is None:
    return 0
  q = collections.deque([node])
  flag = 0
  result = []
  while len(q):
    n = len(q)
    val = []
    for i in range(n):
      root = q.popleft()
      val.append(root.info)

      if root.left:
        q.append(root.left)

      if root.right:
        q.append(root.right)
    if flag == 0:
      flag = 1
    else:
      val.reverse()
      flag = 0
    result.append(val)

  return result

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* ZIG ZAG TRAVERSAL ***************')
  output = zigZagTraversal(t.root)
  print(output)


if __name__ == '__main__':
  main()


# Output:
# -------
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ************* ZIG ZAG TRAVERSAL ***************
# [[10], [30, 20], [40, 50]]
