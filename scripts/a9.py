import numpy as np

arr = np.arange(12).reshape((3, 4))
print(repr(arr))

arr = np.reshape([24, 12, -69, 84, 2, 22, 9, -4], (4, 2))
print(repr(arr))