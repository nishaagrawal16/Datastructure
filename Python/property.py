# Type-1
# property(fget=None, fset=None, fdel=None, doc=None)
# Return value from property()
# The property() method returns a property attribute from the given getter, setter and deleter.
# 1) If no arguments are given, property() method returns a base property attribute that doesn't contain any getter, setter or deleter.
# 2) If doc isn't provided, property() method takes the docstring of the getter function.

class Person(object):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name, 'perseon doc')

p = Person('Nisha')
print(p.name)
p.name = 'Usha'
print(p.name)
# del p.name
# print(p.name)

#Type-2
# Using @property decorator
class Person1(object):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        self._name = n
    
    @name.deleter
    def name(self):
        del self._name

p = Person1('Nisha')
print(p.name)
p.name = 'Usha'
print(p.name)
