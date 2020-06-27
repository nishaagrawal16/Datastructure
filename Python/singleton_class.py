# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

class Singleton:
   __instance = None

   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

s = Singleton()
print(s)
s = Singleton.getInstance()
print(s)
s = Singleton.getInstance()
print(s)


# Using decorator
def singleton(class1):
    instance = {}
    def get_instance():
        if class1 not in instance:
            instance[class1] = class1()
        return instance[class1]
    return get_instance

@singleton
class myClass(object):
    pass

m = myClass()
print(m)

m1 = myClass()
print(m1)

# Output:
# -------
# <__main__.Singleton instance at 0x7f9970627190>
# <__main__.Singleton instance at 0x7f9970627190>
# <__main__.Singleton instance at 0x7f9970627190>
# <__main__.myClass object at 0x7f9970622d10>
# <__main__.myClass object at 0x7f9970622d10>
