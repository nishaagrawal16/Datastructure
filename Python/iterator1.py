# # https://www.programiz.com/python-programming/iterator
# # Create your own iterator.

class IteratorFib:
    def __init__(self, n):
        print('test1')
        self.n = n
        self.count = 0

    def __iter__(self):
        print('tes2')
        return self # It can be any object (either of same class or differnce)
    
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
# ------
# test1
# next of IteratorFib
# 1
# next of IteratorFib
# 2
# ************ Iterator ***************
# tes2
# next of IteratorFib
# 3
# next of IteratorFib
# 4
# next of IteratorFib
# 5
# next of IteratorFib
# Traceback (most recent call last):
#   File "iterator1.py", line 35, in <module>
#     main()
#   File "iterator1.py", line 30, in main
#     print(next(i))
# StopIteration
# 