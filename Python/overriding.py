# Python program to demonstrate error if we 
# forget to invoke __init__() of parent.  
class A(object):
      a = 1
      def __init__(self, n = 'Rahul'):
              print('A')
              self.name = n

class B(A): 
      def __init__(self, roll):
              print('B')
              self.roll = roll
              # If you forget to invoke the __init__()
              # of the parent class then its instance variables would not be available to the
              # child class.
              # The self parameter within super function acts as the object of the parent class
              super(B, self).__init__()
              # OR
              # A.__init__(self)
b = B(23)
print(b.roll)
print(b.name)
print(b.a)


# Python program to demonstrate private members 
# of the parent class 
class C(object): 
       def __init__(self): 
              self.c = 21
  
              # d is private instance variable  
              self.__d = 42    
class D(C): 
       def __init__(self): 
              self.e = 84
              self.__f = 99
              C.__init__(self) 
object1 = D()
print(dir(object1))
# This is the way to call the private variables
print(object1._C__d)
print(object1._D__f)
# produces an error as d is private instance variable 
# print D.d


# Python code to demonstrate multiple inheritance 
# we cannot override a private method of a superclass, which is the one having double underscores before its name. 
# Base Class 
class A(object):                 
        def __init__(self): 
                constant1 = 1
        def __method1(self): 
                print('method1 of class A') 
  
class B(A): 
        def __init__(self): 
                constant2 = 2
                A. __init__(self) 
        def __method1(self): 
                print('method1 of class B')

        def calling1(self): 
                self.__method1() 
                self._A__method1() 
b = B()
# AttributeError: 'B' object has no attribute '__method1'
# b.__method1()

# How to call the private methods of a class.
b._B__method1()
b._A__method1()
print('******* Calling1 **************')
b.calling1()
