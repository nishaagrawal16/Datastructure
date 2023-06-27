"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
        10
       /  \
      20  30
     / \
    40 50
Complexity
----------
Time: O(n)
Space: O(n)
"""

from collections import deque

class Node:
  def __init__(self, value):
    self.val = value
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

class Solution:
  def levelOrder(self, root):
    if root is None:
      return []
    q = deque([root])
    result = []
    while q:
      num_of_nodes = len(q)
      level = []
      while num_of_nodes > 0:
        root = q.popleft()
        level.append(root.val)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
        num_of_nodes -= 1
      result.append(level)
    return result

def main():
  print('***************** Level Order ******************')
  t = Tree()
  t.createTree()
  s = Solution()
  Output = s.levelOrder(t.root)
  print('Output:', Output)


if __name__ == '__main__':
  main()

# Output:
#---------
# ***************** Level Order ******************
# Output: [[10], [20, 30], [40, 50]]
