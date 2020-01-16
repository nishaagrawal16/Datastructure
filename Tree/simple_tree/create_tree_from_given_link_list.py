# Construct Complete Binary Tree from its Linked List Representation
# 1. Create an empty queue.
# 2. Make the first node of the list as root, and enqueue it to the queue.
# 3. Until we reach the end of the list, do the following.
#   a. Dequeue one node from the queue. This is the current parent.
#   b. Traverse two nodes in the list, add them as children of the current parent.
#   c. Enqueue the two nodes into the queue.
# 10 -> 20 -> 30 -> 40 -> 50 -> None
# O(n)


class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None

  def create_list(self):
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    self.start = n1

  def traverse(self):
    p = self.start
    while p is not None:
      print p.info,
      p = p.next
    print('None')


class TreeNode:
  def __init__(self, value):
    self.data = value
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

def create_tree(start):
  que = []
  current = start
  t = Tree()
  t.root = TreeNode(current.info)
  que.append(t.root)
  current = current.next
  while current is not None:
    parent = que.pop(0)
    left_child = None
    right_child = None
    left_child = TreeNode(current.info)
    que.append(left_child)
    current = current.next
    if current is not None:      
      right_child = TreeNode(current.info)
      que.append(right_child)
      current = current.next      
    parent.left = left_child
    parent.right = right_child
    
  print('*********** TRAVERSE TREE ***************') 
  t.treeTraversalInOrder(t.root)

def main():
  link_list = SingleLinkList()
  print('*********** CREATE LIST *****************')
  link_list.create_list()
  print('*********** TRAVERSE LIST ***************')
  link_list.traverse()
  create_tree(link_list.start)
  

if __name__ == '__main__':
  main()


# Output:
# -------
# *********** CREATE LIST *****************
# *********** TRAVERSE LIST ***************
# 10 20 30 40 50 None
# *********** TRAVERSE TREE ***************
# 40 20 50 10 30
