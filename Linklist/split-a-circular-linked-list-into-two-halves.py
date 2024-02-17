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

  def traverse(self):
    if self.start is not None:
      p = self.start
      while p is not None:
        print('%d -> ' % p.info, end='')
        p = p.next
        if p == self.start:
          break
      print('None')
      if p is not None:
        print('starting point:', p.info)

  def splitCircularList(self, list1, list2):
    if self.start is None:
      return
    slow = self.start
    fast = self.start
    # For odd elements fast.next will be start
    # For even elements fast.next.next will be start
    while fast.next != self.start and fast.next.next != self.start:
      fast = fast.next.next
      slow = slow.next

    # If even element then move fast to it's next
    if fast.next.next == self.start:
      fast = fast.next

    # Assign list1 start
    list1.start = self.start

    # Assign list2 start
    if self.start.next != self.start:
      list2.start = slow.next

    # Make lists circular
    slow.next = list1.start
    fast.next = list2.start


def main():
  print('****************** CIRCULAR LINK LIST *****************')
  circular_linklist = LinkList()
  circular_linklist1 = LinkList()
  circular_linklist2 = LinkList()
  print('********************** CREATE LIST ********************')
  circular_linklist.create_link_list()
  circular_linklist.traverse()
  circular_linklist.splitCircularList(circular_linklist1, circular_linklist2)
  print('************************ 1st List *********************')
  circular_linklist1.traverse()
  print('************************ 2nd List *********************')
  circular_linklist2.traverse()


if __name__ == '__main__':
  main()
