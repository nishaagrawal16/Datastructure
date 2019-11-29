#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
# O(n2)

def printPostOrder(preorder, inorder, n):
  if preorder[0] in inorder:
    root = inorder.index(preorder[0])
  else:
    print 'root not found in inorder'
    return

  # Check left subtree present
  if root != 0:
    printPostOrder(preorder[1: root+1],
                   inorder[:root], 
                   len(inorder[:root]))

  # Check right subtree present
  if root != n-1:
    printPostOrder(preorder[root+1:],
                   inorder[root+1:],
                   len(inorder[root+1:]))

  print preorder[0],


def main():
  preorder = [1, 2, 4, 5, 3, 6]
  inorder = [4, 2, 5, 1, 3, 6]
  if len(preorder) == len(inorder):
    n = len(preorder)
  else:
    print 'Preorder and inorder is not of the same tree'
    return
  print('********** PREORDER TRAVERSAL ***********')
  print preorder
  print('********** INORDER TRAVERSAL ************')
  print inorder
  print('********** POSTORDER TRAVERSAL **********')
  printPostOrder(preorder, inorder, n)

if __name__ == '__main__':
  main()