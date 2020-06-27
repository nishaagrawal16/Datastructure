# Create a iterator of different class

class A:
    def __init__(self, data):
        self.num = data.n
        self.count1 = 0

    def next(self):
        print('next of A')
        if self.count1 == self.num:
            raise StopIteration
        self.count1 += 1
        return self.count1

class IteratorFib:
    def __init__(self, n):
        print('test1')
        self.n = n
        self.count = 0

    def __iter__(self):
        print('test2')
        return A(self) # It can be any object (either of same class or different)
    
    def next(self):
        print('next of IteratorFib')
        if self.count == self.n:
            raise StopIteration
        self.count += 1
        return self.count

def main():
    a = IteratorFib(5)
    print(a.next()) # next of IteratorFib (Only working as object.method())
    print(next(a)) # next of IteratorFib (fulfill the next inbuilt functionality but not iterator)
    print('************ Iterator ***************')
    i = iter(a) # test2 (Now call iterator) This the method which create the iterable object
    print(i.next())
    print(next(i))
    print(i.next())
    print(next(i))
    print(i.next())
    print(next(i))

if __name__ == '__main__':
    main()

# Output:
# -------
# test1
# next of IteratorFib
# 1
# next of IteratorFib
# 2
# ************ Iterator ***************
# test2
# next of A
# 1
# next of A
# 2
# next of A
# 3
# next of A
# 4
# next of A
# 5
# next of A
# Traceback (most recent call last):
#   File "test.py", line 41, in <module>
#     print(next(i))
# StopIteration    
