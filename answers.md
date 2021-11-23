1. O NumPy é o pacote básico da linguagem Python que permite trabalhar com arranjos, vetores e matrizes de N dimensões, de uma forma comparável e com uma sintaxe semelhante ao software proprietário [Matlab](https://www.mathworks.com/), mas com muito mais eficiência, e com toda a expressividade da linguagem.

 - Objeto array para a implementação de arranjos multidimensionais
 - Objeto matrix para o cálculo com matrizes
 - Ferramentas para álgebra linear
 - Transformadas de Fourier básicas
 - Ferramentas sofisticadas para geração de números aleatórios.

    Além disso tudo, as classes criadas podem ser facilmente herdadas, permitindo a customização do comportamento (por exemplo, dos operadores típicos de adição, subtração, multiplicação, etc.). O módulo é implementado em linguagem C, o que dá uma grande velocidade às operações realizadas.

2. Criará um array referenciado por um [código de caracteres](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types), útil principalmente para manter a compatibilidade com versões anteriores de pacotes mais antigos, como Numeric. ([link para script](scripts/q2.py))

3. O anterior criará um array com três números, este fará um array contendo dois arrays, com três números cada. ([link para script](scripts/q3.py))

4. Quando um array é referenciado a outro, eles ficam "ligados", ou seja, quando um deles é alterado, o outro também é. Já o copy, não possui tal ligação, então se qualquer um for editado, não afetará o outro.

5. A função `astype` copia o array e molda o array para o tipo especificado como parâmetro. <br> 

    ```python
    newArray = np.array([2, 2, 2.5])
    # OUTPUT array([1., 2., 2.5])
    newArray.astype(int)
    # OUTPUT array([1, 2, 2])
    ```

6. Quando queremos atribuir a uma variável o valor equivalente a Not a Number (NaN).

7. Usamos np.inf quando queremos retornar um ponto flutuante que representa o infinito positivo, já -np.inf quando queremos um ponto flutuante equivalente a infinito negativo.

8. Retorna um array com números entre o invervalo provido.

   Exemplo: `np.arange(0, 10)` é equivalente ao intervalo `[0,5)`, ou seja, o intervalo inclui o número inicial, mas exclui o final.

   [Código do exercício](scripts/q8.py) com uma explicação de cada exemplo:

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

9.  O `np.reshape` faz o que o próprio nome diz, retorna um novo formato do array provido sem alterar seus dados. ([link para script de exemplo](scripts/a9.py))

10. - **np.zeros:** é uma rotina de criação de array e retorna um novo array de zeros com o formato recebido no parâmetro.
    - **np.ones:** retorna um novo array de uns com o formato recebido no parâmetro.
    - **np.zeros_like:** é uma rotina de criação de array e retorna um novo array de zeros com o mesmo formato do array recebido como parâmetro.
    - **np.ones_like:** é uma rotina de criação de array e retorna um novo array de uns com o mesmo formato do array recebido como parâmetro.
    - **np.transpose:** é uma rotina de manipulação de arrays e reverte ou permuta os eixos de um array e asism retorna o array modificado. 
        [Link para script de exemplo](/scripts/a10.py)

11. Aritmética multidimensional é, simplificadamente, um array que contêm outros arrays. Uma vez que um array é um vetor, aritmética multidimensional é um termo que refere-se a uma matriz. ([link para script de exemplo](scripts/a11.py))

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

    ([link para script](scripts/q12.py))

13. Para fazer a multiplicação de matrizes podemos utilizar a rotina de manipulação `numpy.multiply` que irá multiplicar os argumentos das matrizes. [Link para scripe de exemplo.](scripts/a13.py)

14. A grosso modo, o `np.random.seed` torna previsíveis os números aleatórios. Ou seja, você provê uma seed para gerar um pseudo-número "aleatório".

    Um exemplo de usabilidade é quando você precisa depurar um código que utiliza números aleatórios, então você define uma seed para que o código faça sempre a mesma coisa.

    Segue o link de um artigo que explica e exemplifica muito bem o uso do `np.random.seed`: https://www.sharpsightlabs.com/blog/numpy-random-seed/

15. Ele apenas embaralha todo o array.

    Exemplos ([link para script de exemplo](scripts/a15.py)):

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

16. A distribuição normal, também conhecida como distribuição gaussiana, é uma curva simétrica em torno do seu ponto médio, apresentando assim seu famoso formato de sino.<br>
    A distribuição normal pode ser usada para aproximar distribuições discretas de probabilidade, como por exemplo a distribuição binomial. Além disso, a distribuição normal serve também como base para a inferência estatística clássica.


17. ```python
    arr = np.array([[ 0,  2,  3],
                    [ 1,  3, -6],
                    [-3, -2,  1]])
    # repr retorna o um valor representativo ao objeto, no caso irá retornar a string True quando o valor for igual a 3
    print(repr(arr == 3))
    # já aqui irá retornar a string True todo vez que o valor for maior que 0
    print(repr(arr > 0))
    # aqui retornará True quando o objeto for diferente de 1
    print(repr(arr != 1))
    # aqui retornará True quando o valor for igual a 1, o ~ inverteu a lógica
    print(repr(~(arr != 1)))
    ```

18. Basta usar o [`np.concatenate`](https://numpy.org/devdocs/reference/generated/numpy.concatenate.html). ([link para script de exemplo](scripts/a18.py))

19. O [`np.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html) salva o array num arquivo binário, no formato `.npy`. O [`np.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html) faz o contrário, ele carrega os arrays contidos num arquivo `.npy` ou `.npz`.

20. ```python
    arr = np.array([[0,  72,   3],
				[1,   3, -60],
				[-3, -2,   4]])

    # A primeira retorna o menor valor do conjundo de arrays, e a segunda o maior
    print(arr.min())
    print(arr.max())
    # Retorna o menor valor de cada linha de array
    print(repr(arr.min(axis=1)))
    # Retorna a média dos elementos do array
    print(np.mean(arr))
    # Retorna a variância dos elementos do array, uma medida da propagação de uma distribuição
    print(np.var(arr))
    # Retorna a mediana dos elementos do array
    print(np.median(arr))
    
    ```

    Documentação:

    1. https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html
    2. https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html
    3. https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    4. https://numpy.org/doc/stable/reference/generated/numpy.var.html
    5. https://numpy.org/doc/stable/reference/generated/numpy.median.html

    ([link para script](scripts/q20.py))

