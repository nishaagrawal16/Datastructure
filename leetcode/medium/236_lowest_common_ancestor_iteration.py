"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

        3
       /  \
      5    1
     / \  / \
    6   2 0  8
       / \
      7   4

Complexity
----------
Time: O(n)
Space: O(n)
"""

class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None
    self.p = None
    self.q = None

  def createTree(self):
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(1)
    n4 = Node(6)
    n5 = Node(2)
    n6 = Node(7)
    n7 = Node(4)
    n8 = Node(0)
    n9 = Node(8)
    self.root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n6
    n5.right = n7
    n3.left = n8
    n3.right = n9
    self.p = n2
    self.q = n3

  def treeTraversalInOrder(self, root):
    if root:
      self.treeTraversalInOrder(root.left)
      print(root.val, end=' ')
      self.treeTraversalInOrder(root.right)

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    if root is None:
      return None
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
      root = stack.pop()
      if root.left:
        stack.append(root.left)
        parent[root.left] = root
      if root.right:
        stack.append(root.right)
        parent[root.right] = root
    ancestor = set()
    while p:
      ancestor.add(p)
      p = parent[p]

    while q not in ancestor:
      q = parent[q]
    return q


def main():
  print('****************** TREE ****************')
  t = Tree()
  t.createTree()
  print('********** INORDER TRAVERSAL ***********')
  t.treeTraversalInOrder(t.root)
  s = Solution()
  print('\n*** Lowest common Ancestor of 5 & 1 ***')
  p = Node(5)
  q = Node(1)
  Output = s.lowestCommonAncestor(t.root, t.p, t.q)
  print('Output:', Output.val)


if __name__ == '__main__':
  main()

# Output:
#---------
# ****************** TREE ****************
# ********** INORDER TRAVERSAL ***********
# 6 5 7 2 2 3 0 1 8
# *** Lowest common Ancestor of 5 & 1 ***
# Output: 3
