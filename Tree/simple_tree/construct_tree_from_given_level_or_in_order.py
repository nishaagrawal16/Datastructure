# Date: 17-Dec-2019
# Create tree from the given levelorder and inorder.
#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
#
# https://www.geeksforgeeks.org/construct-tree-inorder-level-order-traversals/
# O(n2)


class Node:
  def __init__(self, info):
    self.info = info
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.info, end=' ')
      self.treeTraversalInOrder(root.right)

def buildTree(levelorder, inorder):
  if inorder:
    for i in range(0, len(levelorder)):
      if levelorder[i] in inorder:
        rootIndx = inorder.index(levelorder[i])
        tNode = Node(levelorder[i])
        break
  if not inorder:
    return

  # Creating left subtree present
  tNode.left = buildTree(levelorder, inorder[:rootIndx])

  # Creating right subtree present
  tNode.right = buildTree(levelorder, inorder[rootIndx+1:])
  print('returned info: ', tNode.info)
  return tNode

def main():
  inorder = [4, 2, 5, 1, 3, 6]
  levelorder = [1, 2, 3, 4, 5, 6]
  if len(levelorder) != len(inorder):
    print('levelorder and inorder is not of the same tree')
    return
  print('**************** TREE ******************')
  root = buildTree(levelorder, inorder)
  t = Tree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(root)
  print('')


if __name__ == '__main__':
  main()


# Output:
# -------
# **************** TREE ******************
# returned info:  4
# returned info:  5
# returned info:  2
# returned info:  6
# returned info:  3
# returned info:  1
# ********** INORDER TRAVERSAL ************
# 4 2 5 1 3 6
