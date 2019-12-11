#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
# O(n)


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def treeTraversalPostOrder(self, root, post_order):
    if root:
      self.treeTraversalPostOrder(root.left, post_order)
      self.treeTraversalPostOrder(root.right, post_order)
      post_order.append(root.data)
      print root.data,

def buildTree(preorder, inorder, n):
  if preorder[0] in inorder:
    rootIndx = inorder.index(preorder[0])
    tNode = Node(preorder[0])
  else:
    print 'root not found'
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
  print 'returned data: ', tNode.data
  return tNode
  
def main():
  preorder = [1, 2, 4, 5, 3, 6]
  inorder = [4, 2, 5, 1, 3, 6]
  postorder = [4, 5, 2, 6, 3, 1]
  if len(preorder) == len(inorder):
    if len(preorder) == len(postorder):
      n = len(preorder)
    else:
      print 'Preorder and postorder is not of the same tree'
      return
  else:
    print 'Preorder and inorder is not of the same tree'
    return

  print('**************** TREE ******************')
  root = buildTree(preorder, inorder, n)
  t = Tree()
  print('********** INORDER TRAVERSAL ************')
  post_order = []
  t.treeTraversalPostOrder(root, post_order)
  print('\nGiven Preorder, Inorder and Postorder traversals are of same tree')
  if post_order == postorder:
    print 'Yes'
  else:
    print 'No'


if __name__ == '__main__':
  main()


# Output:
# -------
# **************** TREE ******************
# returned data:  4
# returned data:  5
# returned data:  2
# returned data:  6
# returned data:  3
# returned data:  1
# ********** INORDER TRAVERSAL ************
# 4 5 2 6 3 1 
# Given Preorder, Inorder and Postorder traversals are of same tree
# Yes
