#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
#
# For N nodes, same function is called around N times and each call
# to that function uses <>.index(...) which again takes O(N) so
# effectively complexity is O(N^2)
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

# O(n^2)
def buildTree(preorder, inorder, n):
  if preorder[0] in inorder:
    rootIndx = inorder.index(preorder[0])
    tNode = Node(preorder[0])
  else:
    print('root not found')
    return

  # Creating left subtree present
  if rootIndx != 0:
    tNode.left = buildTree(preorder[1: rootIndx+1],
              inorder[:rootIndx],
              len(inorder[:rootIndx]))

  # Creating right subtree present
  if rootIndx != n-1:
    tNode.right = buildTree(preorder[rootIndx+1:],
                   inorder[rootIndx+1:],
                   len(inorder[rootIndx+1:]))
  print('returned info: ', tNode.info)
  return tNode

# O(n)
def build_tree(preorder, inorder):
  def array_to_tree(left, right):
    nonlocal preIndex

    if left > right:
      return None

    root_value = preorder[preIndex]
    root = Node(root_value)

    preIndex += 1
    root.left = array_to_tree(left, map_of_inorder_value[root_value] - 1)
    root.right = array_to_tree(map_of_inorder_value[root_value] + 1, right)

    return root

  preIndex = 0
  map_of_inorder_value = {}
  for index, value in enumerate(inorder):
    map_of_inorder_value[value] = index

  return array_to_tree(0, len(inorder) - 1)

def main():
  preorder = [1, 2, 4, 5, 3, 6]
  inorder = [4, 2, 5, 1, 3, 6]
  if len(preorder) == len(inorder):
    n = len(preorder)
  else:
    print('Preorder and inorder is not of the same tree')
    return
  print('**************** TREE ******************')
  root = buildTree(preorder, inorder, n)
  t = Tree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(root)
  root = build_tree(preorder, inorder)
  print('\n********** INORDER TRAVERSAL ************')
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
