# Write a program to Calculate height of a tree | Iteration
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
      print root.info,
      self.treeTraversalInOrder(root.right)

# Computes height of a tree 
def height(root): 
  if root is None: 
    return 0 
  
  q = []
  left_count = 0
  right_count = 0
  q.append(root)
  while len(q):
    root = q.pop(0)
    if root.left:
      q.append(root.left)
      left_count = left_count + 1
  
    if root.right:
      q.append(root.right)
      right_count = right_count + 1

  if left_count > right_count:
    return left_count + 1
  else:
    return right_count + 1


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ************')
  t.treeTraversalInOrder(t.root)
  print('\n************* TREE HEIGHT ***************')
  print(height(t.root))


if __name__ == '__main__':
  main()


# Output:
# -------
# 
# ***************** TREE ******************
# 
# ********** INORDER TRAVERSAL ************
# 40 20 50 10 30 
# ************* TREE HEIGHT ***************
# 3
