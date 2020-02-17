# Check whether Loop is present or not
# Find the starting point of the loop
# Input:
# 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 40 -> 50 ->60 -> 40 -> 50...
# Output:
# Starting point: 40

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class LinkList:
  def __init__(self):
    self.start = None
    
  def create_list_with_loop(self):
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n6 = Node(60)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n3
    self.start = n1

  def traverse(self):
    p = self.start
    i = 0
    while p is not None and i<10:
      print('%d -> ' % p.info)
      p = p.next
      i = i + 1
    print('None')

  def findLoopWithStartingPoint(self):
    slow = self.start
    fast = self.start
    p1 = self.start
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        print('slow/fast pointer meet at', slow.info)
        p2 = slow
        while True:
          if p1.info == p2.info:
            print('intersection/starting point of loop: ', p1.info)
            return True
          else:
            p1 = p1.next
            p2 = p2.next    
    return False

def main():
  link_list = LinkList()
  link_list.create_list_with_loop()
  link_list.traverse()
  result = link_list.findLoopWithStartingPoint()
  if not result:
    print('no loop present')

if __name__ == '__main__':
  main()
