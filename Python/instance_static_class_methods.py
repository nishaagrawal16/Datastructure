import inspect
class A(object):
    def f(self, x):
        return 2 * x

    @staticmethod
    def s():
        pass

    @classmethod
    def c(cls):
        pass
print('********* instance method *********')
print(A.f)
print(A.f.__class__)
print(inspect.isfunction(A.f))
print(inspect.ismethod(A.f))
print('********* static method *********')
print(A.s)
print(A.s.__class__)
print(inspect.isfunction(A.s))
print(inspect.ismethod(A.s))
print('********* class method *********')
print(A.c)
print(A.c.__class__)
print(inspect.isfunction(A.c))
print(inspect.ismethod(A.c))

print(A.f(1, 7))

# Output:
# -------
# Python 2
# ********* instance method *********
# <unbound method A.f>
# <type 'instancemethod'>
# False
# True
# ********* static method *********
# <function s at 0x7f970392ba50>
# <type 'function'>
# True
# False
# ********* class method *********
# <bound method type.c of <class '__main__.A'>>
# <type 'instancemethod'>
# False
# True
# 
# Python 3
# ********* instance method *********
# <function A.f at 0x7f01ec8a17a0>
# <class 'function'>
# True
# False
# ********* static method *********
# <function A.s at 0x7f01ec8a18c0>
# <class 'function'>
# True
# False
# ********* class method *********
# <bound method A.c of <class '__main__.A'>>
# <class 'method'>
# False
# True

# Difference between   python2 and python 3
# A.instance_method    unbound     function
# A.class_method       Bound       Bound
# A.static_method      function    function
