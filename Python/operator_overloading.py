# https://www.programiz.com/python-programming/operator-overloading
# Must Read This.

class Point:
    def __init__(self, x):
        self.x = x
 
    def __str__(self):
      return 'Point (%d)' % (self.x)
 
    def __add__(self, other):
        return (Point(self.x + other.x))
 
p1 = Point(5)
p2 = Point(6)
print(p1 + p2)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(5, 8)
v2 = Vector(4, -2)
print(v1 + v2)

# Output:
# -------
# Point (11)
# Vector (9, 6)
