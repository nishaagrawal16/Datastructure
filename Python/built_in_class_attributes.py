# Built-in Class Attributes:
class Student:
  pass 
 
class Employee(Student):
   '''Common base class for all employees'''
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     '''C employees'''
     print("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

e = Employee('nisha', 100)
print('__dict__: ', Employee.__dict__)
print('__name__: ', Employee.__name__)
print('__module__:', Employee.__module__)
print('__bases__: ', Employee.__bases__)

print('__dict__: ', e.__dict__)
print('__module__:', e.__module__)

# Output:
# -------
# __dict__:  {'__module__': '__main__', '__doc__': 'Common base class for all employees',
#             'empCount': 1, '__init__': <function Employee.__init__ at 0x0000000001E69048>,
#             'displayCount': <function Employee.displayCount at 0x0000000001E690D0>,
#             'displayEmployee': <function Employee.displayEmployee at 0x0000000001E69158>}
# __name__:  Employee
# __module__: __main__
# __bases__:  (<class '__main__.Student'>,)
# __dict__:  {'name': 'nisha', 'salary': 100}
# __module__: __main__
