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

  def insert(self, value):
    temp = Node(value)
    # List is empty
    if self.start is None:
      print('empty')
      temp.next = temp
      self.start = temp
      return
    p = self.start
    # List has only one node
    if p.next == self.start:
      print('1 element')
      temp.next = p
      self.start = temp
      p.next = temp
      return

    # List has more than one nodes
    while p is not None:
      if p.next == self.start:
        temp.next = p.next
        p.next = temp
        break
      else:
        p = p.next

  def insert_at(self, k, val):
    temp = Node(val)
    i = 1
    p = self.start
    while i < k-1:
        p = p.next
        i += 1
    temp.next = p.next
    p.next = temp

  def delete_from_end(self):
    # Check list is empty
    if self.start is None:
      print('List is empty')
      return

    # List has 1 element
    p = self.start
    if p.next == self.start:
      self.start = None
      return

    # Delete last Element
    while p and p.next and p.next.next:
      if p.next.next == self.start:
        p.next = self.start
        break
      else:
        p = p.next

  def delete_at_starting(self):
    # Check list is empty
    if self.start is None:
      print('List is empty')
      return

    # List has 1 element
    p = self.start
    if p.next == self.start:
      self.start = None
      return

    current = self.start
    p = self.start
    while p is not None:
      if p.next == current:
        p.next = current.next
        self.start = p.next
        break
      else:
        p = p.next

  def traverse(self):
    if self.start is not None:
      p = self.start
      while p is not None:
        print('%d -> ' % p.info, end='')
        p = p.next
        if p == self.start:
          break
      print ('None')
      print('starting point:', p.info)


def main():
  print('****************** CIRCULAR LINK LIST *****************')
  circular_linklist = LinkList()
  print('********************** CREATE LIST ********************')
  circular_linklist.create_link_list()
  circular_linklist.traverse()
  print('*********** INSERT At 8th position ********************')
  circular_linklist.insert_at(8, 22)
  circular_linklist.traverse()

  circular_linklist1 = LinkList()
  print('*********** INSERT TO AN EMPTY LIST ********************')
  circular_linklist1.insert(1)
  circular_linklist1.traverse()
  print('*********** INSERT TO A LIST WHICH HAS 1 ELEMENT *******')
  circular_linklist1.insert(2)
  circular_linklist1.traverse()
  print('******************** INSERT AT END *********************')
  circular_linklist1.insert(3)
  circular_linklist1.traverse()
  print('******************** DELETE AT STARTING ****************')
  circular_linklist1.delete_at_starting()
  circular_linklist1.traverse()
  print('******************** DELETE FROM END *******************')
  circular_linklist1.delete_from_end()
  circular_linklist1.traverse()


if __name__ == '__main__':
  main()
