class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {"name": self.name, "age": self.age}

    def __str__(self):
        return "Person(name=" + self.name + ", age=" + str(self.age) + ")"


p = Person("abc", 21)
print("***** __str__() example **********")
print(p)
print(str(p))
print(p.__str__())

print("***** __repr__() example **********")
# Traceback (most recent call last):
#   File "str_vs_repr.py", line 22, in <module>
#     print(repr(p)) # this will throw an error as typeError
# TypeError: __repr__ returned non-string (type dict)
# print(repr(p)) # this will throw an error as typeError
print(type(p.__repr__()))
print(p.__repr__())

# Difference between __str__ and __repr__ functions
# 1) __str__ must return string object whereas __repr__ can return any python expression like list, tuple, dict.
# 2) If __str__ implementation is missing then __repr__ function is used as fallback.
#    There is no fallback if __repr__ function implementation is missing.
# 3) If __repr__ function is returning String representation of the object,
#    we can skip implementation of __str__ function.

# Here repr() is returning a string and str() is missing so repr() is used in str() also.
# >>> class A(object):
# ...     def __repr__(self):
# ...             return "{'a': 1, 'b': 2}"
# ...
# >>> a = A()
# >>> a
# {'a': 1, 'b': 2}
# >>> print(a)
# {'a': 1, 'b': 2}
# >>> print(a.__str__())
# {'a': 1, 'b': 2}
# >>> print(str(a))
# {'a': 1, 'b': 2}
# >>> print(repr(a))
# {'a': 1, 'b': 2}
# >>> print(a.__repr__())
# {'a': 1, 'b': 2}


# Output:
# -------
# ***** __str__() example **********
# Person(name=abc, age=21)
# Person(name=abc, age=21)
# Person(name=abc, age=21)
# ***** __repr__() example **********
# <class 'dict'>
# {'name': 'abc', 'age': 21}
