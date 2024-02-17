# Create a iterator of different class


class A:
    def __init__(self, data):
        self.num = data.n
        self.count1 = 0

    def next(self):
        print("next of A")
        if self.count1 == self.num:
            raise StopIteration
        self.count1 += 1
        return self.count1


class IteratorFib:
    def __init__(self, n):
        print("test1")
        self.n = n
        self.count = 0

    def __iter__(self):
        print("test2")
        return A(self)  # It can be any object (either of same class or different)

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
    i = a.__iter__()
    # test2 (Now call iterator) This the method which create the iterable object
    print(i.next())
    print(i.next())
    print(i.next())
    print(i.next())
    print(i.next())
    print(i.next())


if __name__ == "__main__":
    main()

# Output:
# -------
# test1
# next of IteratorFib
# 1
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
#   File "/usr/local/google/home/nishaa/Documents/git_hub_2022/Datastructure/Python/iterator2.py", line 51, in <module>
#     main()
#   File "/usr/local/google/home/nishaa/Documents/git_hub_2022/Datastructure/Python/iterator2.py", line 47, in main
#     print(i.next())
#           ^^^^^^^^
#   File "/usr/local/google/home/nishaa/Documents/git_hub_2022/Datastructure/Python/iterator2.py", line 12, in next
#     raise StopIteration
# StopIteration
