# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)

class QueueList:
    def __init__(self, n):
        self.maxSize = n
        self.que = [0]*n
        self.front = -1
        self.rear = -1
    
    def isQueueEmpty(self):
        return self.rear == -1 and self.front == -1
        
    def isQueueFull(self):
        return self.rear == self.maxSize - 1
        
    def enqueue(self, value):
        if self.isQueueFull():
            raise Exception('Queue is full')
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
print('Dequeued element: ', qL.dequeue())
print('Dequeued element: ', qL.dequeue())
print('Element for dequeue: ', qL.peek())

# Output:
# ------
# Queue is empty:  True
# Queue is Full:  False
# Dequeued element:  a
# Dequeued element:  b
# Element for dequeue:  c
