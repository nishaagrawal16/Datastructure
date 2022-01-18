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
        if self.top == -1:
            raise Exception("Stack is empty")
        return False
        
    def isStackFull(self):
        if self.top == self.maxSize - 1:
            raise Exception("Stack is full")
        return False
            
    def size(self):
        return self.top + 1
        
    def topPosition(self):
        return self.top

    def push(self, val):
        if not self.isStackFull():
            self.top += 1
            self.st[self.top] = val
        
    def pop(self):
        if not self.isEmpty():
            val = self.st[self.top]
            self.top -= 1
            return val
        
    def peep(self):
        i = self.top
        while i > -1:
            print(self.st[i])
            i -= 1

st = Stack(6)
try:
    print('Stack is empty or not: ', st.isEmpty())
except Exception as err:
    print(err)
try:
    print('Pop the element from stack: ', st.pop())
except Exception as err:
    print(err)
    
st.push('a')
st.push('b')
print('Top position of stack: ', st.topPosition())
print('Size of stack', st.size())
st.push('c')
st.push('d')
st.push('e')
st.push('f')
try:
    st.push('g')
except Exception as err:
    print(err)
print('Pop the element from stack: ', st.pop())
print('Size of stack', st.size())
print('Top position of stack: ', st.topPosition())
st.peep()

# Output:
# -------
# Stack is empty
# Stack is empty
# Top position of stack:  1
# Size of stack 2
# Stack is full
# Pop the element from stack:  f
# Size of stack 5
# Top position of stack:  4
# e
# d
# c
# b
# a
