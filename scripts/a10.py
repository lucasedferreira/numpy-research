import numpy as np

print(np.zeros(5))
print(np.ones(5))

x = np.arange(6)
print(np.zeros_like(x))
print(np.ones_like(x))

print(np.transpose(x, (1, 0, 2, 5, 4)))
x = x.reshape((2, 3))
print(np.transpose(x))