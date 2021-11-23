import numpy as np

arr = np.array([[0,  72,   3],
				[1,   3, -60],
				[-3, -2,   4]])
# A primeira retorna o menor valor do conjundo de arrays, e a segunda o maior
print(arr.min())
print(arr.max())
# Retorna um array contendo os menores valores de cada linha de array
print(repr(arr.min(axis=1)))
# Retorna a média dos elementos do array
print(np.mean(arr))
# Retorna a variância dos elementos do array, uma medida da propagação de uma distribuição
print(np.var(arr))
# Retorna a mediana dos elementos do array
print(np.median(arr))