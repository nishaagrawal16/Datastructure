import time

a = [1, 2, 3, 4, 5]

# List comprehension approach
start = time.time()
for i in range(0, 500000):
    a = [value if value % 2 == 1 else value * 1 for value in a]
end = time.time()
print(end - start)

# Looping approach
start = time.time()
for i in range(0, 500000):
    for j in range(len(a)):
        if a[j] % 2 == 1:
            a[j] = a[j]
        else:
            a[j] = a[j] * 1

end = time.time()
print(end - start)

## List comprehenson is faster than normal for loop.
# (test-env) ~/code/Datastructure master$ python Python/list_compre.py
# 0.3283200263977051
# 0.5858590602874756
# (test-env) ~/code/Datastructure master$ python Python/list_compre.py
# 0.3186030387878418
# 0.5762190818786621
# (test-env) ~/code/Datastructure master$ python Python/list_compre.py
# 0.31956005096435547
# 0.5985069274902344
# (test-env) ~/code/Datastructure master$ python Python/list_compre.py
# 0.3128180503845215
# 0.616724967956543
