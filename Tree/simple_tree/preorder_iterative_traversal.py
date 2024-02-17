# Preorder Traversal (Root, Left, Right)
# https://www.youtube.com/watch?v=Bfqd8BsPVuw&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=11#
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

  def treeTraversalPreOrder(self):
    s = [self.root]
    while s:
      root = s.pop()
      print(root.data, end=' ')
      if root.right:
        s.append(root.right)
      if root.left:
        s.append(root.left)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** PREORDER TRAVERSAL ************')
  t.treeTraversalPreOrder()
  print('')


if __name__ == '__main__':
  main()


# Output:
# -------
# ***************** TREE ******************
#
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
