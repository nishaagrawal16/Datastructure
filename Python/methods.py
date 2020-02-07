
class A:
    name = 'nisha'
    def __init__(self, n):
        self.name = n

    def foo(self):
        print('name: ', self.name, A.name)
        print('A instance method')

    @classmethod
    def class_foo(cls):
        A.name = "hello"
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
print(a)
print(a.foo)
print(a.class_foo)
print(a.static_foo)

# <bound method A.foo of <__main__.A instance at 0x7f3d6b1a0d20>>
# <bound method classobj.class_foo of <class __main__.A at 0x7f3d6b19c590>>
# <function static_foo at 0x7f3d6b1a58d0>

a.foo()
a.class_foo()
a.static_foo()
A.class_foo()
A.static_foo()


print(a.name)
print(A.name)
a.change_name()
a.foo()
