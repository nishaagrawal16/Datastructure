"""TODO(nishaa): DO NOT SUBMIT without one-line documentation for circular_link_list.

TODO(nishaa): DO NOT SUBMIT without a detailed description of circular_link_list.
"""

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None

class LinkList:
  def __init__(self):
    self.start = None

  def create_link_list(self):
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    self.start = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1

  def insert_at_begining(self, value):
    temp = Node(value)
    # List is empty
    if self.start is None:
      temp.next = temp
      self.start = temp
      return
    p = self.start
    # List has only one node
    if p.next == self.start:
      temp.next = p
      self.start = temp
      p.next = self.start

  def traverse(self):
    if self.start is not None:
      p = self.start
      while (True):
        print('%d -> ' % p.info),
        p = p.next
        if p == self.start:
          break

def main():
  circular_linklist = LinkList()
  # circular_linklist.create_link_list()
  circular_linklist.insert_at_begining(1)
  circular_linklist.insert_at_begining(2)
  circular_linklist.traverse()

if __name__ == '__main__':
  main()
