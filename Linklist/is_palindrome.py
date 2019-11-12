# we solve this problem using recurson in which left and right two pointer point to the start of the node.
# then call isPalindrome(left, right.next) untill right will become None
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
      print('%c -> ' % p.info, end=" ")
      p = p.next
    print('None')

  def isPalindrome(self):
    left = self.start
    right = self.start
    rsp, left = self.isPalindromeCheck(left, right)
    if rsp:
      print('Palindrome')
    else:
      print('not Palindrome')

  def isPalindromeCheck(self, left, right):
    if right is None:
      return True, left
    rsp, left = self.isPalindromeCheck(left, right.next)
    if not rsp:
      return False, left
    print(left.info, right.info)
    rsp = (left.info == right.info)
    return rsp, left.next
    
link_list = SingleLinkList()
print('*********** CREATING LIST ***************')
link_list.create_list()

print('*********** TRAVERSE LIST ***************')
link_list.traverse()

link_list.isPalindrome()
