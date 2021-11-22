1. 

2. Criará um array referenciado por um [código de caracteres](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types), útil principalmente para manter a compatibilidade com versões anteriores de pacotes mais antigos, como Numeric. ([link para script](scripts/q2.py))

3. O anterior criará um array com três números, este fará um array contendo dois arrays, com três números cada. ([link para script](scripts/q3.py))

4. Quando um array é referenciado a outro, eles ficam "ligados", ou seja, quando um deles é alterado, o outro também é. Já o copy, não possui tal ligação, então se qualquer um for editado, não afetará o outro.

5. 

6. 

7. 

8. Retorna um array com números entre o invervalo provido.

   Exemplo: `np.arange(0, 10)` é equivalente ao intervalo `[0,5)`, ou seja, o intervalo inclui o número inicial, mas exclui o final.

   [Código do exercício](https://www.minecraft.net/ko-kr) com uma explicação de cada exemplo:

   ```python
   # Cria um array de números inteiros, [0, 1, 2, 3, 4]
   arr = np.arange(5)
   
   # Cria um array de números decimais, [0.0, 1.0, 2.0, 3.0, 4.0]
   arr = np.arange(5.1)
   
   # Cria um array de números inteiros começando em -1, [-1, 0, 1, 2, 3]
   arr = np.arange(-1, 4)
   
   # Cria um array de números decimais começando em -1.5 com intervalo de 2 números, [-1.5, 0.5, 2.5]
   arr = np.arange(-1.5, 4, 2)
   ```

9. O `np.reshape` faz o que o próprio nome diz, retorna um novo formato do array provido sem alterar seus dados. ([link para script de exemplo](https://www.minecraft.net/ko-kr))

10. 

11. Aritmética multidimensional é, simplificadamente, um array que contêm outros arrays. Uma vez que um array é um vetor, aritmética multidimensional é um termo que refere-se a uma matriz. ([link para script de exemplo](https://www.minecraft.net/ko-kr))

12. ```python
    arr = np.array([[2, 4], [6, 9]])
    # Calcula o exponencial¹ de cada elemento. np.exp²
    print(repr(np.exp(arr)))
    # Calcula 2**p (2^p), sendo p cada elemento do array. np.exp2³
    print(repr(np.exp2(arr)))
    
    arr2 = np.array([[1, 10], [np.e, np.pi]])
    # Calcula o logaritmo⁴ natural de cada elemento. np.log⁵
    print(repr(np.log(arr2)))
    # Calcula o logaritmo de base 10 de cada elemento. np.log10⁶
    print(repr(np.log10(arr2)))
    # Eleva o primeiro parâmetro à todos os números do segundo parâmetro. np.power⁷
    print(repr(np.power(3, arr2)))
    # Eleva todos os elementos ao quadrado.
    print(repr(arr**2))
    ```

    Documentação:

    1. https://en.wikipedia.org/wiki/Exponential_function
    2. https://numpy.org/doc/stable/reference/generated/numpy.exp.html
    3. https://numpy.org/doc/stable/reference/generated/numpy.exp2.html
    4. https://en.wikipedia.org/wiki/Logarithm
    5. https://numpy.org/doc/stable/reference/generated/numpy.log.html
    6. https://numpy.org/doc/stable/reference/generated/numpy.log10.html
    7. https://numpy.org/doc/stable/reference/generated/numpy.power.html

    ([link para script](https://www.minecraft.net/ko-kr))

13. 

14. A grosso modo, o `np.random.seed` torna previsíveis os números aleatórios. Ou seja, você provê uma seed para gerar um pseudo-número "aleatório".

    Um exemplo de usabilidade é quando você precisa depurar um código que utiliza números aleatórios, então você define uma seed para que o código faça sempre a mesma coisa.

    Segue o link de um artigo que explica e exemplifica muito bem o uso do `np.random.seed`: https://www.sharpsightlabs.com/blog/numpy-random-seed/

15. Ele apenas embaralha todo o array.

    Exemplos ([link para script de exemplo](https://www.minecraft.net/ko-kr)):

    ```python
    arr = np.arange(10)
    print(repr(np.random.shuffle(arr)))
    # [1 7 5 2 9 4 3 6 0 8]
    
    arr2 = np.arange(10).reshape((3, 3))
    print(repr(np.random.shuffle(arr2)))
    # [ [3, 4, 5],
    #   [6, 7, 8],
    #	[0, 1, 2] ]
    ```

    

16. 

17. 

18. Basta usar o [`np.concatenate`](https://numpy.org/devdocs/reference/generated/numpy.concatenate.html). ([link para script de exemplo](https://www.minecraft.net/ko-kr))

16. O [`np.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html) salva o array num arquivo binário, no formato `.npy`. O [`np.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html) faz o contrário, ele carrega os arrays contidos num arquivo `.npy` ou `.npz`.

