# Date: 13-Dec-2019
# Sum of precedence of Nodes
#         10(120)
#       /     \
#      20(90)  30(30)
#     /     \
#    40(40) 50(50)
# O(n)
# TODO

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

  def SumOfPrecedence(self, root):
    if root:
      precedence_sum = 0
      self.SumOfPrecedence(root.left)
      self.SumOfPrecedence(root.right)
      print(root.info, end=' ')
      if root.left:
        precedence_sum = precedence_sum + root.left.info
      if root.right:
        precedence_sum = precedence_sum + root.right.info
      if precedence_sum:
        root.info = precedence_sum
      print("Sum of nodes precedence: ", root.info)

  def sumOfPrecedenceWithOutRecursion(self, root):
    if root is None:
      return
    s = []
    s.append(root)
    while True:
      if root.left:
        s.append(root.left)
        root = root.left
      elif s:
        precedence_sum = 0
        root = s.pop()
        print(root.info, end=' ')
        if root.left:
          precedence_sum = precedence_sum + root.left.info
        if root.right:
          precedence_sum = precedence_sum + root.right.info
        if precedence_sum:
          root.info = precedence_sum
        print("Sum of nodes precedence: ", root.info)
        if root.right:
          root = root.right
      else:
        break


def main():
  print('***************** TREE ******************\n')
  t = Tree()
  t.createTree()
  t.SumOfPrecedence(t.root)
  # t.sumOfPrecedenceWithOutRecursion(t.root)


if __name__ == '__main__':
  main()


# Output:
# -------
#
# ***************** TREE ******************
#
# 40 Sum of nodes precedence:  40
# 50 Sum of nodes precedence:  50
# 20 Sum of nodes precedence:  90
# 30 Sum of nodes precedence:  30
# 10 Sum of nodes precedence:  120

