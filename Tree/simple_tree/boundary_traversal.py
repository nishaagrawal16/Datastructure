# Boundary Travesal
# https://www.youtube.com/watch?v=0ca1nvR0be4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=21#
#
# Anti-clockwise
# left boundary excluding leaf nodes
# Leaf nodes
# right boundary in reverse order excluding leaf nodes
#         10
#       /   \
#      20   30
#     / \
#    40 50
# Time Complexity: O(n)
# TODO
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

def leftView(node, result):
  q = collections.deque([node])
  while len(q):
    n = len(q)
    val = []
    for i in range(n):
      root = q.popleft()
      if i == 0:
        val.append(root.info)
      if root.left:
        q.append(root.left)

      if root.right:
        q.append(root.right)
    result.append(val)

# def leftView(root, result):
#   # q = collections.deque([root])
#   s = []
#   while True:
#     if root.left is None and root.right is None:
#       break
#     s.append(root)
#     if root.left:
#       s.append(root.left)
#     elif root.right:
#       s.append(root.right)
#     root = root.left
#   for val in s:
#     print('left view: ', val.info)


def boundaryTraversal(node):
  if node is None:
    return 0
  result = []
  leftView(node, result)
  # while



  return result

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* ZIG ZAG TRAVERSAL ***************')
  output = boundaryTraversal(t.root)
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
