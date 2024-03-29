#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
# O(n)


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

  def treeTraversalPostOrder(self, root, post_order):
    if root:
      self.treeTraversalPostOrder(root.left, post_order)
      self.treeTraversalPostOrder(root.right, post_order)
      post_order.append(root.info)
      print(root.info, end=' ')

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
  def array_of_tree(left, right):
    nonlocal preIndex
    if left > right:
      return None

    root_value = preorder[preIndex]
    root = Node(root_value)
    preIndex += 1
    root.left = array_of_tree(left, map_of_inorder_value[root_value] - 1)
    root.right = array_of_tree(map_of_inorder_value[root_value] + 1, right)

    return root

  preIndex = 0
  map_of_inorder_value = {}
  for index, value in enumerate(inorder):
    map_of_inorder_value[value] = index
  return array_of_tree(0, len(inorder) - 1)

def main():
  preorder = [1, 2, 4, 5, 3, 6]
  inorder = [4, 2, 5, 1, 3, 6]
  postorder = [4, 5, 2, 6, 3, 1]
  if len(preorder) == len(inorder):
    if len(preorder) == len(postorder):
      n = len(preorder)
    else:
      print('Preorder and postorder is not of the same tree')
      return
  else:
    print('Preorder and inorder is not of the same tree')
    return

  print('**************** TREE ******************')
  root = buildTree(preorder, inorder, n)
  t = Tree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(root)
  post_order = []
  print('\n********** POST ORDER TRAVERSAL ************')
  t.treeTraversalPostOrder(root, post_order)
  root = build_tree(preorder, inorder)
  print('\n********** POST ORDER TRAVERSAL ************')
  t.treeTraversalPostOrder(root, post_order)
  if post_order == postorder:
    print('\nGiven Preorder, Inorder and Postorder traversals are of same tree')
  else:
    print('\nGiven Preorder, Inorder and Postorder traversals are not of same tree')


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
# 4 5 2 6 3 1
# Given Preorder, Inorder and Postorder traversals are of same tree
