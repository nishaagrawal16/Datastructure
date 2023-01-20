# Date: 17-Dec-2019
# Create tree from the given levelorder and inorder.
#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
#
# https://www.geeksforgeeks.org/construct-tree-inorder-level-order-traversals/
# O(n^3)


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

# O(n^3)=> n: recursion, n: for loop, n: index()
def buildTree(levelorder, inorder):
  if not inorder:
    return
  for i in range(len(levelorder)):
    if levelorder[i] in inorder:
      rootIndx = inorder.index(levelorder[i])
      tNode = Node(levelorder[i])
      break

  # Creating left subtree present
  tNode.left = buildTree(levelorder, inorder[:rootIndx])

  # Creating right subtree present
  tNode.right = buildTree(levelorder, inorder[rootIndx+1:])
  print('returned info: ', tNode.info)
  return tNode

# O(n^2)
def build_tree(levelorder, inorder):
  if not inorder:
    return None

  # Use map instead of index() because it use O(n) complexity
  map_of_inorder_value = {v: i for i, v in enumerate(inorder)}
  # Use set insetead of list because it use O(n) complexity
  # when using the in operator
  inorder_set = set(inorder)
  for i in range(len(levelorder)):
    if levelorder[i] in inorder_set:
      rootIndx = map_of_inorder_value[levelorder[i]]
      root = Node(levelorder[i])
      break

  # Creating left subtree present
  root.left = build_tree(levelorder, inorder[:rootIndx])

  # Creating right subtree present
  root.right = build_tree(levelorder, inorder[rootIndx+1:])
  return root

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
  root = build_tree(levelorder, inorder)
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
# ********** INORDER TRAVERSAL ************
# 4 2 5 1 3 6
