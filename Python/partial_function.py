from functools import partial

def power(base, expo):
  print('{} base to the power of {}'.format(base, expo))
  return base ** expo

square = partial(power, expo=2)
cube = partial(power, expo=3)

print(square(3))
print(cube(3))
