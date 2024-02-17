# Check balance binary tree
# left_height - right_height <= 1
# https://www.youtube.com/watch?v=Yt50Jfbd8Po&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=16
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
    # n4.left = n5

  def checkBalanced(self, root):
    if root is None:
      return 0
    lh = self.checkBalanced(root.left)
    if lh == -1:
      return -1
    rh = self.checkBalanced(root.right)
    if rh == -1:
      return -1
    if lh - rh > 1:
      return -1
    return 1 + max(lh, rh)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** Check Balanced Binary Tree ************')
  result = t.checkBalanced(t.root)
  if result == -1:
    print('Not Balanced')
  else:
    print('Balanced Tree')


if __name__ == '__main__':
  main()


# Output:
# -------
# ***************** TREE ******************

# ********** Check Balanced Binary Tree ************
# Balanced Tree
