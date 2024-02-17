matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
]
print(matrix)

# Using comprehension
li = [item for row in matrix for item in row]
print("Using list Comprehension....")
print(li)

# Using extend method
result = []
for row in matrix:
    result.extend(row)
print("Using extend Method....")
print(result)


# Using chain method of itertools
from itertools import chain

print("Using chain method.....")
print(list(chain.from_iterable(matrix)))

# Using reduce method
from functools import reduce
from operator import add

print("Using reduce method.....")
print(list(reduce(lambda x, y: x + y, matrix)))

print(list(reduce(add, matrix)))
