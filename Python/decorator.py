
def decoWrapper1(func):
    def xyz():
        print('start')
        func()
    return xyz

@decoWrapper1
def print_hello1():
    print('Hello')

print('***************** decorator with function only ********************')
print_hello1()

# Output:
# ------
# ***************** decorator with function only ********************
# start
# Hello

# With function arguments
def decoWrapper2(func):
    def xyz(arg):
        print('start', arg)
        func(arg)
    return xyz

@decoWrapper2
def print_hello2(name):
    print('Hello', name)

print('***** decorator with function and one argument to the function *******')
print_hello2('nisha')

# Output:
# -------
# ***** decorator with function and one argument to the function *******
# ('start', 'nisha')
# ('Hello', 'nisha')

# With two arguments by using *
def decoWrapper3(func):
    def xyz(*arg):
        print('start', arg)
        func(*arg)
    return xyz

@decoWrapper3
def print_hello3(*name):
    print('Hello', name)

print('***** decorator with function and two argument to the function *******')
print_hello3('nisha', 'agrawal')

# Output:
# -------
# ***** decorator with function and two argument to the function *******
# ('start', ('nisha', 'agrawal'))
# ('Hello', ('nisha', 'agrawal'))

def decoWrapper4(a, b):
    def xyz(func):
        def abc(name):
            print('start', a, b)
            func(name)
        return abc
    return xyz

@decoWrapper4(10, 20)
def print_hello4(name):
    print('Hello', name)

print('***** decorator with arguments and function with one argument *******')
print_hello4('nisha')

# Output:
# ------
# ***** decorator with arguments and function with one argument *******
# ('start', 10, 20)
# ('Hello', 'nisha')
