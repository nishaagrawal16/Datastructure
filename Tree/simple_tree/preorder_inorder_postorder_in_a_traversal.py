# Preorder, Inorder and Postorder traversal
# https://www.youtube.com/watch?v=ySp2epYvgTE&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=14#         10
#        10
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

  def treeTraversal(self):
    s = [(self.root, 1)]
    preorder = []
    inorder = []
    postorder = []
    while s:
      current, num = s.pop()
      if num == 1:
        # Preorder
        num += 1
        s.append((current, num))
        preorder.append(current.data)
        if current.left:
          s.append((current.left, 1))
      elif num == 2:
        # Inorder
        num += 1
        s.append((current, num))
        inorder.append(current.data)
        if current.right:
          s.append((current.right, 1))
      elif num == 3:
        # Postorder
        postorder.append(current.data)
    print('Preorder: ', preorder)
    print('Inorder: ', inorder)
    print('Postorder: ', postorder)


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** TREE TRAVERSAL ************')
  t.treeTraversal()
  print('')


if __name__ == '__main__':
  main()


# Output:
# -------
# ***************** TREE ******************
#
# ********** TREE TRAVERSAL ************
# Preorder:  [10, 20, 40, 50, 30]
# Inorder:  [40, 20, 50, 10, 30]
# Postorder:  [40, 50, 20, 30, 10]
