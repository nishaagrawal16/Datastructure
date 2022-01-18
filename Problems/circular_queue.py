# Circular queue

class QueueList:
    def __init__(self, n):
        self.maxSize = n
        self.que = [0]*n
        self.front = -1
        self.rear = -1
    
    def isQueueEmpty(self):
        return self.rear == -1 and self.front == -1
        
    def isQueueFull(self):
        return self.rear == self.front - 1 or (self.rear == self.maxSize - 1 and self.front == 0)
        
    def enqueue(self, value):
        if self.isQueueFull():
            raise Exception('Queue is full')
        if self.rear == self.maxSize - 1 and self.front != 0:
            self.rear = -1
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.que[self.rear] = value
            
    def dequeue(self):
        if self.isQueueEmpty():
            raise Exception('Queue is Empty')
        val = self.que[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return val
            
    def peek(self):
        return self.que[self.front]

qL = QueueList(4)
print('Queue is empty: ', qL.isQueueEmpty())
print('Queue is Full: ', qL.isQueueFull())
qL.enqueue('a')
qL.enqueue('b')
qL.enqueue('c')
qL.enqueue('d')
print('Queue is Full: ', qL.isQueueFull())
print('Remove element: ', qL.dequeue())
qL.enqueue('e')
print('front: ', qL.front)
print('rear: ', qL.rear)
print('Queue is Full: ', qL.isQueueFull())
print('Remove element: ', qL.dequeue())
print('Element for dequeue: ', qL.peek())
print('Queue is Full: ', qL.isQueueFull())
qL.enqueue('f')
print('Queue is Full: ', qL.isQueueFull())
try:
    qL.enqueue('g')
except Exception as err:
    print('Can not add element in queue: ', err)

# Output:
# ------
# Queue is empty:  True
# Queue is Full:  False
# Queue is Full:  True
# Remove element:  a
# front:  1
# rear:  0
# Queue is Full:  True
# Remove element:  b
# Element for dequeue:  c
# Queue is Full:  False
# Queue is Full:  True
# Can not add element in queue:  Queue is full
