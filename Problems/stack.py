# Stack
# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

class Stack:
    def __init__(self, n):
        self.maxSize = n
        self.top = -1
        self.st = [0]*n
        
    def empty(self):
        if self.top == -1:
            return True
        return False
        
    def size(self):
        return self.top + 1
        
    def topPosition(self):
        return self.top

    def push(self, val):
        if self.top == self.maxSize - 1:
            print('stack is full')
        else:
            self.top += 1
            self.st[self.top] = val
        
    def pop(self):
        if self.empty():
            print('Stack is empty')
            return
        else:
            val = self.st[self.top]
            self.top -= 1
            return val
        
    def printStack(self):
        for i in range(self.top + 1):
            print(self.st[i])
st = Stack(6)
print('Stack is empty or not: ', st.empty())
st.push('a')
st.push('b')
print('Top position of stack: ', st.topPosition())
print('Size of stack', st.size())
st.push('c')
st.push('d')
print('Pop the element from stack: ', st.pop())
print('Size of stack', st.size())
print('Top position of stack: ', st.topPosition())
st.printStack()

# Output:
# -------
# Stack is empty or not:  True
# Top position of stack:  1
# Size of stack 2
# Pop the element from stack:  d
# Size of stack 3
# Top position of stack:  2
# a
# b
# c
