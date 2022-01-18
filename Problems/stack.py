# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
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
        
    def isEmpty(self):
        return self.top == -1
        
    def isStackFull(self):
        return self.top == self.maxSize - 1
            
    def size(self):
        return self.top + 1

    def push(self, val):
        if self.isStackFull():
            raise Exception('Stack is full')
        self.top += 1
        self.st[self.top] = val
        
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        val = self.st[self.top]
        self.top -= 1
        return val

    def peek(self):
        return self.st[self.top]

st = Stack(6)
print('Stack is empty or not: ', st.isEmpty())
try:
    print('Pop the element from stack: ', st.pop())
except Exception as err:
    print('Can not pop: ', err)
    
st.push('a')
st.push('b')
print('Size of stack', st.size())
st.push('c')
st.push('d')
st.push('e')
st.push('f')
try:
    st.push('g')
except Exception as err:
    print('Can not add element: ', err)
print('Pop the element from stack: ', st.pop())
print('Size of stack', st.size())
print('Top element: ', st.peek())

# Output:
# -------
# Stack is empty or not:  True
# Can not pop:  Stack is empty
# Size of stack 2
# Can not add element:  Stack is full
# Pop the element from stack:  f
# Size of stack 5
# Top element:  e
