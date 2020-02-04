# https://www.programiz.com/python-programming/generator
# Print fibonacci series

class Solutions(Exception):
    def fibonacci_series(self, n):
        a, b = 0, 1
        while b <= n:
            yield b
            a, b = b, a + b


def main():
    s = Solutions()
    # When called, it returns an object (iterator) but does not start execution immediately.
    f = s.fibonacci_series(20)

    # try:
    #     while True:
    #         print(f.next())
    # except StopIteration:
    #     print('finish')
    #
    #     OR
    #
    # Note: One final thing to note is that we can use generators with for loops directly.
    # This is because, a for loop takes an iterator and iterates over it using next() function.
    # It automatically ends when StopIteration is raised.    
    for item in f:    
        print(item)


if __name__ == '__main__':
    main()
