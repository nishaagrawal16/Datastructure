class Parent(object):
    def __init__(self):
        print("In parent class")
 
    def myMethod(self):
        print("I am defining in Parent class")
 
    def display(self):
        print("displaying...")
 
class Child(Parent):
    def __init__(self):
        print("In Child class")
        self.__priv_variable = 10
 
    def myMethod(self):
        print("I am defining in Child class")
 
def poly(ob):
    ob.myMethod()
    
ch = Child()
ch.myMethod() #method overriding
ch.display()  #Inheritance
print(ch._Child__priv_variable) #data encapsulation
p = Parent()
poly(p) #polymorphism
poly(ch)

