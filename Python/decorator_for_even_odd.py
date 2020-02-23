# Write a decorator for a function which returns a number between 1 to 100
# check whether the returned number is even or odd in decorator function.
import random

def decoCheckNumber(func):
    print ('Inside the decorator')
    def xyz():
        print('*************** Inside xyz *********************')
        num = func()
        print(num)
        if num %2 != 0: # Odd
            print('number is odd')
        else:
            print('number is Even')
    return xyz

@decoCheckNumber
def random_number():
    return random.randrange(1, 100)

for i in range(10):
    random_number()
