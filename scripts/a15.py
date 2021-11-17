import numpy as np

arr = np.arange(10)
print(repr(np.random.shuffle(arr)))
# [1 7 5 2 9 4 3 6 0 8]

arr2 = np.arange(9).reshape((3, 3))
print(repr(np.random.shuffle(arr2)))
# [ [3, 4, 5],
#   [6, 7, 8],
#	[0, 1, 2] ]