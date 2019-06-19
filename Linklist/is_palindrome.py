# we solve this problem using recurson in which left and right two pointer point to the start of the node.
# then call isPalindrom(left, right.next) untill right will become None
# check left.info == right.info after returning from None to the right pointer. Right pointer will go from null to 1 node
# TODO
class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None
    self.count = 0

  def create_list(self):
    n1 = Node('R')
    n2 = Node('A')
    n3 = Node('D')
    n4 = Node('A')
    n5 = Node('R')
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    self.start = n1

  def traverse(self):
    p = self.start
    while p is not None:
      print(p.info, end=" ")
      p = p.next
    print('\n')

  def isPalindrom(self):    
    left = self.start
    right = self.start
    print('count: ', self.count)
    if self.isPalindromCode(left, right):
      print('Palindrom')
    else:
      print('Not Palindrom')
  # Not right program
  def isPalindromCode(self, left, right):
    self.count = self.count + 1
    print('hello')
    # After reaching right to None
    if right is None:
      return True
    # Only right has to point to the next in each call.
    rsp = self.isPalindromCode(left, right.next)
    if not rsp:
      return False
    rsp_info = (left.info == right.info)
    print(left.info, right.info, )
    left = left.next
    print(left.info)
    return rsp_info 
    
linkList = SingleLinkList()
print('*********** CREATING LIST ***************')
linkList.create_list()

print('*********** TRAVERSE LIST ***************')
linkList.traverse()

linkList.isPalindrom()