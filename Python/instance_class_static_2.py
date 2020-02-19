class A(object):
    def instanc_method(self):
        print('I am instance_method')
    @classmethod
    def class_method(cls):
        print('I am class method')
    @staticmethod
    def static_method():
        print('I am static method')


a = A()
print('************** Instance method ********************')
print(a.instanc_method)
a.instanc_method()
print(A.instanc_method)
A.instanc_method(a)
print('************** class method ********************')
print(a.class_method)
a.class_method()
print(A.class_method)
A.class_method()
print('************** static method ********************')
print(a.static_method)
a.static_method()
print(A.static_method)
A.static_method()

# Output:
# -------
# ************** Instance method ********************
# <bound method A.instanc_method of <__main__.A object at 0x0000000002286160>>
# I am instance_method
# <function A.instanc_method at 0x0000000002288048>
# I am instance_method
# ************** class method ********************
# <bound method A.class_method of <class '__main__.A'>>
# I am class method
# <bound method A.class_method of <class '__main__.A'>>
# I am class method
# ************** static method ********************
# <function A.static_method at 0x0000000002288158>
# I am static method
# <function A.static_method at 0x0000000002288158>
# I am static method
