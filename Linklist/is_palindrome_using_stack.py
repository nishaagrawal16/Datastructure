# We solve this problem by using stack in which slow and fast two pointer point
# to the start of the node. Then move slow pointer once and store slow.info in
# the stack and fast pointer 2 times.

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class SingleLinkList:
  def __init__(self):
    self.start = None

  def create_list(self, li):
    if self.start is None:
      self.start = Node(li[0])
    p = self.start
    for i in range(1,len(li)):
      temp = Node(li[i])
      p.next = temp
      p = p.next

  def traverse(self):
    p = self.start
    while p is not None:
      print('%c -> ' % p.info, end='')
      p = p.next
    print('None')

  def isPalindrom(self):
    slow = self.start
    fast = self.start
    stack = []
    while fast and fast.next:
      stack.append(slow.info)
      slow = slow.next
      fast = fast.next.next
    # For odd number of element in list we have to ignore
    # the middle element. So need to move to the slow by next.
    if fast is not None:
      slow = slow.next
    while stack:
      if stack.pop() != slow.info:
        print('Not Palindrome')
        return
      slow = slow.next
    print('palindrome')

def main():
  link_list = SingleLinkList()
  print('*********** CREATING LIST ***************')
  link_list.create_list(['R', 'A', 'D', 'A', 'R'])

  print('*********** TRAVERSE LIST ***************')
  link_list.traverse()

  link_list.isPalindrom()

if __name__ == '__main__':
  main()
