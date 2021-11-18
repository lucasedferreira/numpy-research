import numpy as np

arr = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6]])
print(repr(np.concatenate((arr, arr2))))