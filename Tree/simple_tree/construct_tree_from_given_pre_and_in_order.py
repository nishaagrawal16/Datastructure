#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
# Need to ask the complexity
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print root.data, 
      self.treeTraversalInOrder(root.right)

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
  if len(preorder) == len(inorder):
    n = len(preorder)
  else:
    print 'Preorder and inorder is not of the same tree'
    return
  print('**************** TREE ******************')
  root = buildTree(preorder, inorder, n)
  t = Tree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(root)

if __name__ == '__main__':
  main()
