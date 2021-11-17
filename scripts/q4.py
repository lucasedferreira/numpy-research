import numpy as np

a = np.array([0, 1])
b = np.array([2, 3])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 99
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = -11
print('Array b: {}'.format(repr(b)))