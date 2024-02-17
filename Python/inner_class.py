# Inner class can not access the attributes and methods of outer class.
class A:
    def __init__(self):
        print("In Parent Class init")
        self.db = self.Inner()

    def display(self):
        print("In Parent Class")

    # this is inner class
    class Inner:
        def __init__(self):
            print("In Inner Class init")

        def display1(self):
            print("Inner Of Parent Class")


a = A()
print("A DIR: ", dir(a))
print("Inner DIR: ", dir(a.Inner))
a.display()
inside = a.db
inside.display1()

# Output:
# -------
# In Parent Class init
# In Inner Class init
# ('A DIR: ', ['Inner', '__doc__', '__init__', '__module__', 'db', 'display'])
# ('Inner DIR: ', ['__doc__', '__init__', '__module__', 'display1'])
# In Parent Class
# Inner Of Parent Class
print("************************ NEXT QUESTION **********************")


class A(object):
    def __init__(self):
        self.db = self.Inner()
        print("INNER DIR**********: ", dir(self.db))

    def display(self):
        print("In Parent Class")

    # this is inner class
    class Inner:
        def display1(self):
            print("Inner Of Parent Class")


class B(A):
    def __init__(self):
        print("In Child Class")
        super(B, self).__init__()

    class Inner(A.Inner):
        def display2(self):
            print("Inner Of Child Class")


# creating child class object
p = B()
print("B DIR: ", dir(p))
p.display()

# create inner class object
x = p.db
print("Inner DIR: ", dir(x))
x.display1()
x.display2()

# Output:
# -------
# In Child Class
# ('INNER DIR**********: ', ['__doc__', '__module__', 'display1', 'display2'])
# ('B DIR: ', ['Inner', '__class__', '__delattr__', '__dict__', '__doc__',
# '__format__', '__getattribute__', '__hash__', '__init__', '__module__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'db', 'display'])
# In Parent Class
# ('Inner DIR: ', ['__doc__', '__module__', 'display1', 'display2'])
# Inner Of Parent Class
# Inner Of Child Class
#
