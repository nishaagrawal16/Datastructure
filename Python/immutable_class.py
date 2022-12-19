# Avoid monkey patching
# Create a immutable class

class A:
    def __init__(self, name):
        super().__setattr__('name', name)

    def __setattr__(self, a, b):
        msg = '"%s" has no attribute "%s"' % (self.__class__.__name__, a)
        raise AttributeError(msg)


a = A('Nisha')
print(a.name)
a.age = 12

# Output:
# --------
#
# Nisha
# Traceback (most recent call last):
#   File "<string>", line 14, in <module>
# File "<string>", line 9, in __setattr__
# AttributeError: "A" has no attribute "age"
