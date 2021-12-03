def numberOfBits(n):
    i = 0; a = 0
    while a < n:
        a = a + 2**i
        i = i + 1
    return i

print(numberOfBits(10))
