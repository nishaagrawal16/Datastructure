class Person(object):
    def __init__(self, name, age):
        self.full_name = name
        self.age = age

p = Person('Nisha', 31)
print(getattr(p, 'full_name'))
setattr(p, 'age', 34)
print(p.age)
print(p.__dict__)

# Output:
# -------
# Nisha
# 34
# {'full_name': 'Nisha', 'age': 34}
