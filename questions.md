1. O que é NumPy?

2. O que fará o programa a seguir:

```python
import numpy as np
arr = np.array([-9, 1, 7], dtype=np.float32)
print(repr(arr))
```



3. Qual a diferença do programa da questão número para o programa a seguir:

```python
import numpy as np
arr = np.array([[10, 11, 12], [21, 22, 23]],
dtype=np.float32)
print(repr(arr))
```



4. Quando fazemos referência a um array o que o Python faz? E qual a diferença para o copy?

```python
a = np.array([0, 1])
b = np.array([2, 3])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 99
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = -11
print('Array b: {}'.format(repr(b)))
```

5. O que faz a função astype (dê um exemplo)

6. Quando devemos usar np.nan?

7. Explique np.inf e -np.inf

8. Explique o funcionamento de arange

```python
arr = np.arange(5)
print(repr(arr))

arr = np.arange(5.1)
print(repr(arr))

arr = np.arange(-1, 4)
print(repr(arr))

arr = np.arange(-1.5, 4, 2)
print(repr(arr))
```



9. Faça um exemplo de código com np.reshape

10. Para que serve np.transpose, np.zeros, np.ones, np.zeros_like, np.ones_like - aproveite e de um exemplo de cada em um programa?

11. O que é aritmética multidimensional com python e dê um exemplo de como usar

12. Explique a linha de código abaixo da linha pontilhada no programa a seguir

```python
arr = np.array([[2, 4], [6, 9]])
\# ...................................
print(repr(np.exp(arr)))
\# ...................................
print(repr(np.exp2(arr)))

arr2 = np.array([[1, 10], [np.e, np.pi]])
\# .....................................
print(repr(np.log(arr2)))
\# ...................................
print(repr(np.log10(arr2)))
\#...................................
print(repr(np.power(3, arr2)))
\#...................................
print(repr(arr**2))
```



13. Como fazer a multiplicação de matrizes usando Numpy?

14. Por que usamos np.random.seed?

15. O que faze e como funciona np.random.shuffle?

16. O que é uma distribuição "normal"?

```python
print(np.random.uniform())
print(np.random.uniform(low=-1.5, high=2.2))
print(repr(np.random.uniform(size=3)))
print(repr(np.random.uniform(low=-3.4, high=5.9,
size=(2, 2))))
```



17. Explique o programa usando as linhas pontilhadas

```python
arr = np.array([[ 0,  2,  3],
				[ 1,  3, -6],
				[-3, -2,  1]])
\# .............................................
print(repr(arr == 3))
\# .............................................
print(repr(arr > 0))
\# .............................................
print(repr(arr != 1))
\# .............................................
print(repr(~(arr != 1)))
```



18. Como somar e concatenar arrays?

19. Como funciona np.save e np.load?

20. Use as linhas pontilhadas para explicar

```python
arr = np.array([[0,  72,   3],
				[1,   3, -60],
				[-3, -2,   4]])
\# .............................................
print(arr.min())
print(arr.max())
\# .............................................
print(repr(arr.min(axis=1)))
\# .............................................
print(np.mean(arr))
\# .............................................
print(np.var(arr))
\# .............................................
print(np.median(arr))
```