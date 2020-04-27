import copy

# Shallow copy
# https://docs.python.org/2/library/copy.html
# A shallow copy constructs a new compound object and then (to the extent
# possible) inserts references into it to the objects found in the original.
# Means insert refernces of the inner objects also.
l1 = [[1,2], 3, 4, [5, 6, 7]]
l2 = copy.copy(l1)
l2[0][0] = 8
print('************** SHALLOW COPY **************')
print(l1)
print(l2)
l2[1] = 12
print(l1)
print(l2)

# A deep copy constructs a new compound object and then, recursively, inserts
# copies into it of the objects found in the original.
# Means only copy the inner objects.
l3 = [[1,2], 3, 4, [5, 6, 7]]
l4 = copy.deepcopy(l1)
l4[0][0] = 8
print('**************** DEEP COPY ***************')
print(l3)
print(l4)

l5 = [1, 2, 3, 4, 5, 6, 7]
l6 = copy.copy(l5)
l6[0] = 8
print('******** NO COMPOUND SHALLOW COPY ********')
print(l5)
print(l6)

l7 = [1, 2, 3, 4, 5, 6, 7]
l8 = copy.deepcopy(l7)
l8[0] = 8
print('********** NO COMPOUND DEEP COPY *********')
print(l7)
print(l8)

# Output:
# -------
# ************** SHALLOW COPY **************
# [[8, 2], 3, 4, [5, 6, 7]]
# [[8, 2], 3, 4, [5, 6, 7]]
# **************** DEEP COPY ***************
# [[1, 2], 3, 4, [5, 6, 7]]
# [[8, 2], 3, 4, [5, 6, 7]]
# ******** NO COMPOUND SHALLOW COPY ********
# [1, 2, 3, 4, 5, 6, 7]
# [8, 2, 3, 4, 5, 6, 7]
# ********** NO COMPOUND DEEP COPY *********
# [1, 2, 3, 4, 5, 6, 7]
# [8, 2, 3, 4, 5, 6, 7]
