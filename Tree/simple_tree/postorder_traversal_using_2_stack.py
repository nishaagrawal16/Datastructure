# Postorder traversal (Left, Right, Root)
# https://www.youtube.com/watch?v=2YBhNLodD8Q&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=14
#         10
#       /   \
#      20   30
#     / \
#    40 50
# O(n)
#TODO

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

  # def treeTraversalPostOrder(self):
  #   s1 = [self.root]
  #   s2 = []
  #   while s1:
  #     root = s1.pop()
  #     s2.append(root)
  #     if root.left:
  #       s1.append(root.left)
  #     if root.right:
  #       s1.append(root.right)
  #   while s2:
  #     print(s2.pop().data, end=' ')

  def treeTraversalPostOrder(self):
    current = self.root
    s = []
    while True:
      if current is not None:
        s.append(current)
        current = current.left
      elif s:
        current = s.pop()
        if current.right:
          s.append(current)
          s.append(current.right)
          # current = current.right
      else:
        break

def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** POSTORDER TRAVERSAL ************')
  t.treeTraversalPostOrder()
  print('')


if __name__ == '__main__':
  main()


# Output:
# -------
# ***************** TREE ******************
#
# ********** POSTORDER TRAVERSAL ************
# 40 50 20 30 10
