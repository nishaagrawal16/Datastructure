# Method Resolution Order(MRO)
# https://makina-corpus.com/python/python-tutorial-understanding-python-mro-class-search-path
# 1) Old style: when object is not the parent class as we are using python2.
#               We follow the DLR or depth-first left to right In which we first go
#               to the parent and grand parent if available than left to right.
#
# 2) New Style Python(3.x & 2.3) : Where object is the parent class or either
#   in python2 or python3. We follow the depth first left to right with good
#   head concept as well as C3 linearization algorithm for getting the right
#   mro concept.

# Old Style:
class X:
    def who_am_i(self):
        print("I am a X")

class Y:
    def who_am_i(self):
        print("I am a Y")

class A(X, Y):
    def who_am_i(self):
        print("I am a A")

class B(Y, X):
     def who_am_i(self):
         print("I am a B")

class F (A, B):
    def who_am_i(self):
        print("I am a F")
f = F()
print('************ OLD STYLE *****************')
f.who_am_i()


# Output:
# ------
# ************ OLD STYLE *****************
# I am a F


# New Style:
class X(object):
    def who_am_i(self):
        print("I am a X")

class Y(object):
    def who_am_i(self):
        print("I am a Y")

class A(X, Y):
    def who_am_i(self):
        print("I am a A")

class B(Y, X):
     def who_am_i(self):
         print("I am a B")

class F (A, B):
    def who_am_i(self):
        print("I am a F")
f = F()
print('************ NEW STYLE *****************')
f.who_am_i()

# Output:
# -------
# Traceback (most recent call last):
#   File "mro.py", line 55, in <module>
#     class F (A, B):
# TypeError: Error when calling the metaclass bases
#     Cannot create a consistent method resolution
# order (MRO) for bases X, Y

# Explaination: Using C3 Linearization
# F(A,B) = F + merge(L[A]+L[B] , A, B)
#        = F + merge((A, X, Y) + (B, Y, X), A, B)
#        = FA + merge((X, Y) + (B, Y, X), B)
#        = FAB + merge((X, Y)+ (Y, X))
#        = Cann't create the mro()
