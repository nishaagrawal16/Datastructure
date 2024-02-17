# Check trees are identical or not
# https://www.youtube.com/watch?v=BhuvF_-PWS0&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=19
#
#         10
#       /   \
#      20   30
#     / \
#    40 50
# O(n)


class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.data, end=' ')
      self.treeTraversalInOrder(root.right)

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

  def checkIdenticalTree(self, p, q):
    if p is None or q is None:
      return p == q
    return (p.data == q.data and
           self.checkIdenticalTree(p.left, q.left) and
           self.checkIdenticalTree(p.right, q.right))


def main():
  print('***************** TREE ******************')
  t1 = Tree()
  t1.createTree()
  print('**************** TREE-1 *****************')
  t1.treeTraversalInOrder(t1.root)
  t2 = Tree()
  t2.createTree()
  print('\n**************** TREE-2 *****************')
  t1.treeTraversalInOrder(t2.root)
  result = t1.checkIdenticalTree(t1.root, t2.root)
  if result:
    print('\nTrees are identicals')
  else:
    print('\nTrees are not identicals')


if __name__ == '__main__':
  main()


# Output:
# -------
# ***************** TREE ******************
# **************** TREE-1 *****************
# 40 20 50 10 30
# **************** TREE-2 *****************
# 40 20 50 10 30
# Trees are identicals
