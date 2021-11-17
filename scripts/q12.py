import numpy as np

arr = np.array([[2, 4], [6, 9]])
# Calcula o exponencial de todos os elementos
print(repr(np.exp(arr)))
# Calcula 2**p (2^p), sendo p os elementos
print(repr(np.exp2(arr)))

arr2 = np.array([[1, 10], [np.e, np.pi]])
# .....................................
print(repr(np.log(arr2)))
# ...................................
print(repr(np.log10(arr2)))
#...................................
print(repr(np.power(3, arr2)))
#...................................
print(repr(arr**2))