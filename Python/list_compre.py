import time

a = [1, 2, 3, 4, 5]

start = time.time()

for i in range(0, 500000):
    a = [value if value % 2 == 1 else value * 1 for value in a]

end = time.time()

print(end - start)

start = time.time()

for i in range(0, 500000):
    for j in range(len(a)):
        if a[j] % 2 == 1:
            a[j] = a[j]
        else:
            a[j] = a[j] * 1

end = time.time()

print(end - start)

# List comprehenson is faster than normal for loop.