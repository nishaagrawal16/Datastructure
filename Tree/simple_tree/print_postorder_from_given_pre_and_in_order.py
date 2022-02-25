#         1
#       /   \
#      2     3
#     / \     \
#    4  5      6
# For N nodes, same function is called around N times and each call
# to that function uses <>.index(...) which again takes O(N) so
# effectively complexity is O(N^2)
# O(n2)

def printPostOrder(preorder, inorder, n):
  if preorder[0] in inorder:
    root = inorder.index(preorder[0])
  else:
    print('root not found in inorder')
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

  print(preorder[0], end='')


def main():
  preorder = [1, 2, 4, 5, 3, 6]
  inorder = [4, 2, 5, 1, 3, 6]
  if len(preorder) == len(inorder):
    n = len(preorder)
  else:
    print('Preorder and inorder is not of the same tree')
    return
  print('********** PREORDER TRAVERSAL ***********')
  print('Preorder: ', preorder)
  print('********** INORDER TRAVERSAL ************')
  print('Inorder: ', inorder)
  print('********** POSTORDER TRAVERSAL **********')
  printPostOrder(preorder, inorder, n)
  print('')

if __name__ == '__main__':
  main()


# Output:
# -------
#
# ********** PREORDER TRAVERSAL ***********
# Preorder:  [1, 2, 4, 5, 3, 6]
# ********** INORDER TRAVERSAL ************
# Inorder:  [4, 2, 5, 1, 3, 6]
# ********** POSTORDER TRAVERSAL **********
# 4 5 2 6 3 1
