# Max Heap
# https://www.geeksforgeeks.org/max-heap-in-python/
# insert O(logn)
# getMax O(1)
# extractMax O(logn)
# parent i//2
# leftChild 2*i
# rightChild 2*i+1

import sys
class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.front = 1
        self.heap = [0]*(max_size + 1)
        # Here we have taken the index from 1 to make it simple.
        self.heap[0] = self.heap[0] = float('Inf')

    def leftChild(self, pos):
        return 2*pos

    def rightChild(self, pos):
        return 2*pos + 1

    def parent(self, pos):
        return pos//2

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.size

        # Check for parent element to maintain the max heap property
        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMax(self):
        popped = self.heap[self.front]
        # Replace the 1st element from the last then correct the position
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.heapify(self.front)
        # del self.heap[self.size + 1]
        return popped
    
    def isLeaf(self, pos):
        if pos >= self.size//2 and pos <= self.size:
            return True
        return False

    def heapify(self, pos):
        # If the node is a non-leaf node and smaller 
        # than any of its child 
        if not self.isLeaf(pos):
            if (self.heap[pos] < self.heap[self.leftChild(pos)] or
                self.heap[pos] < self.heap[self.rightChild(pos)]):
                # Check that left child id greater than right child
                # so it should be swapped to the current position.
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                else:                
                    self.swap(pos, self.rightChild(pos))
                    self.heapify(self.rightChild(pos))
    
    def print_heap(self):
        for i in range(1, self.size//2 + 1):
            print('Parent: %d Left child: %d Right Child: %d' %
                 (self.heap[i], self.heap[2*i], self.heap[2*i+1]))
        print(self.heap)
        

def main():
    max_heap = MaxHeap(9)
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(17)
    max_heap.insert(10)
    max_heap.insert(84)
    max_heap.insert(19)
    max_heap.insert(6)
    max_heap.insert(22)
    max_heap.insert(9)
    print('**************** MAX HEAP *****************')
    max_heap.print_heap()
    max_heap.extractMax()
    print('************* AFTER EXTRACTION ************')
    max_heap.print_heap()


if __name__ == '__main__':
    main()
