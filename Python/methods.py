
class A:
    name = 'nisha'
    def __init__(self, n):
        self.name = n

    def foo(self):
        print('A instance method name: ', self.name, A.name)

    @classmethod
    def class_foo(cls):
        A.name = 'hello'
        print('A class method', cls.name)

    @staticmethod
    def static_foo():
        A.name = 'yes'
        print('A static method', A.name)

    def change_name(self):
        self.name = 'll'
        print('in change_name: ', self.name)

a = A('nn')
print(dir(a))
a.foo()
a.class_foo()
a.static_foo()
A.class_foo()
A.static_foo()
print(a.name)
print(A.name)
a.change_name()
a.foo()

# Output:
# -------
# ['__doc__', '__init__', '__module__', 'change_name', 'class_foo', 'foo',
# 'name', 'static_foo']
# ('A instance method name: ', 'nn', 'nisha')
# ('A class method', 'hello')
# ('A static method', 'yes')
# ('A class method', 'hello')
# ('A static method', 'yes')
# nn
# yes
# ('in change_name: ', 'll')
# ('A instance method name: ', 'll', 'yes')
