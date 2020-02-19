class A:
  g_data = []
 
  def __init__(self, data):
    self.g_data.append(data)
 
  def __call__(self):
    for d in self.g_data:
      print (d)
 
a1 = A("Nisha")
a2 = A("Mahabeer")
a3 = A("Khargosh")
print ("*********A(Test)**********")
A("Test")
print ("*********a3()**********")
a3()
print ("*********A(Test1)()**********")
A("Test1")()
 
# Output:
# ------
# *********A(Test)**********
# *********a3()**********
# Nisha
# Mahabeer
# Khargosh
# Test
# *********A(Test1)()**********
# Nisha
# Mahabeer
# Khargosh
# Test
# Test1
