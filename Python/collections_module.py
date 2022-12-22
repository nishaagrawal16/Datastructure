from collections import Counter, defaultdict, OrderedDict, namedtuple

li = [1, 2, 1, 1, 2, 3, 4, 12, 1, 2, 3]
################# Counter #####################
print('Counter: ', Counter(li))

################# defaultdict ##################
d = defaultdict(int)
print(d)
d['one'] = 1
d['two'] = 2
print('defaultdict: ', d)
print(d['three'])

################# OrderedDict ##################
order = OrderedDict()

order['b'] = 2
order['a'] = 1
order['c'] = 3
order['l'] = 12
print('OrderedDict: ', order)

################# namedtuple ##################
nt = namedtuple('Student', 'fname, lname, age')
print('nt: ', nt)
st = nt('nisha', 'agrawal', 34)
print(st.fname)

# Output:
# ------
# Counter:  Counter({1: 4, 2: 3, 3: 2, 4: 1, 12: 1})
# defaultdict(<class 'int'>, {})
# defaultdict:  defaultdict(<class 'int'>, {'one': 1, 'two': 2})
# 0
# OrderedDict:  OrderedDict([('b', 2), ('a', 1), ('c', 3), ('l', 12)])
# nt:  <class '__main__.Student'>
# nisha
