# https://www.programiz.com/python-programming/iterator
# Create your own iterator.
# https://www.programiz.com/python-programming/iterator#for-loop-working
# Must Read: How for loop actually works?, Python Infinite Iterators


class IteratorFib:
    def __init__(self, n):
        print("test1")
        self.n = n
        self.count = 0

    def __iter__(self):
        print("test2")
        return self  # It can be any object (either of same class or different)

    def next(self):
        print("next of IteratorFib")
        if self.count == self.n:
            raise StopIteration
        self.count += 1
        return self.count


def main():
    a = IteratorFib(5)
    print(a.next())  # next of IteratorFib (Only working as object.method())

    print("************ Iterator ***************")
    # test2 (Now call iterator) This the method which create the iterable object
    i = a.__iter__()
    print(i.next())
    print(i.next())
    print(i.next())
    print(i.next())
    # print(i.next())


if __name__ == "__main__":
    main()

# Output:
# ------
# test1
# next of IteratorFib
# 1
# ************ Iterator ***************
# test2
# next of IteratorFib
# 2
# next of IteratorFib
# 3
# next of IteratorFib
# 4
# next of IteratorFib
# 5
# next of IteratorFib
# Traceback (most recent call last):
#   File "/usr/local/google/home/nishaa/Documents/git_hub_2022/Datastructure/Python/iterator1.py", line 40, in <module>
#     main()
#   File "/usr/local/google/home/nishaa/Documents/git_hub_2022/Datastructure/Python/iterator1.py", line 36, in main
#     print(i.next())
#           ^^^^^^^^
#   File "/usr/local/google/home/nishaa/Documents/git_hub_2022/Datastructure/Python/iterator1.py", line 20, in next
#     raise StopIteration
# StopIteration
