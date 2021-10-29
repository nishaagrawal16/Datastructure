#!/usr/bin/python

# Date: 202110-29
#
# Description:
# Implement singleton class.
#
# Approach:
# A decorator function created which checks if instance of decorated class
# already created or not. If not created, creates a new one otherwise returns
# same object.


def singleton(classname):
  """Decorator function which restricts decorated class to be singleton.

  Args:
    classname: Reference of class whose object needs to be created.

  Returns: Instance of requested class.
  """
  instances = {}

  def getInstance(*args, **kwargs):
    """Creates (if not already created) and returns object of a class."""
    if classname not in instances:
      instances[classname] = classname(*args, **kwargs)
    return instances[classname]
  return getInstance


@singleton
class MyClass():
  pass


obj1 = MyClass()
print(id(obj1))

obj2 = MyClass()
print(id(obj2))

# Output:
# ******************
# 139931649436416
# 139931649436416
