# Doubly link list

class Node:
  def __init__(self, value):
    self.info = value
    self.next = None
    self.prev = None

class LinkList:
  def __init__(self):
    self.start = None

  def create_list(self, li):
    if self.start is None:
      self.start = Node(li[0])
    p = self.start
    for i in range(1,len(li)):
      temp = Node(li[i])
      temp.prev = p
      p.next = temp      
      p = p.next

  def traverse(self):
    p = self.start
    while p is not None:
      print('%d -> ' % p.info)
      p = p.next
    print('None')

  def countNodes(self):
    p = self.start
    count = 0
    while p is not None:
      count = count + 1
      p = p.next
    return 
  
  def insert_at_the_end(self, value):
    temp = Node(value)
    p = self.start
    while p.next is not None:
      p = p.next
    temp.prev = p
    p.next = temp

  def insert_at_begining(self, value):
    temp = Node(value)
    temp.next = self.start
    self.start = temp

  def insert_after(self, value, position):
    p = self.start
    temp = Node(value)
    i = 1
    while p.next is not None and i < position - 1: # iterat 2 times
      p = p.next
      i = i + 1
    p.next.prev = temp
    temp.next = p.next
    temp.prev = p
    p.next = temp

     
def main():
  print('********** LIST ***************')
  link_list = LinkList()
  link_list.create_list([10,20,30,40,50])
  link_list.traverse()
  print('******** INSERT AT END *******')
  link_list.insert_at_the_end(60)
  link_list.traverse()
  print('****** INSERT AT BEGINING *****')
  link_list.insert_at_begining(5)
  link_list.traverse()
  print('** INSERT AT GIVEN POSITION **')
  link_list.insert_after(25, 4)
  link_list.traverse()


if __name__ == '__main__':
  main()

# Output
# -------
# ********** LIST-1 ***************
# 10 ->  20 ->  30 ->  40 ->  50 ->  None

