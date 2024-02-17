# Maximum Path Sum
# https://www.youtube.com/watch?v=WszrfSwMz58&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=18
#
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

def maxPathSum(node, d):
  if node is None:
    return 0
  # Ignore negative nodes
  left_sum = max(0, maxPathSum(node.left, d))
  right_sum = max(0, maxPathSum(node.right, d))
  d[0] = max(d[0], (left_sum + right_sum + node.info))
  return node.info + max(left_sum, right_sum)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* MAXIMUM PATH SUM ***************')
  d = [0]
  h = maxPathSum(t.root, d)
  print(d[0])


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************

# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30
# ************* MAXIMUM PATH SUM ***************
# 110
