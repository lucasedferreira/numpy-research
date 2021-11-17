1. 

2. Criará um array referenciado por um [código de caracteres](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types), útil principalmente para manter a compatibilidade com versões anteriores de pacotes mais antigos, como Numeric. ([link para script](https://www.minecraft.net/ko-kr))

3. O anterior criará um array com três números, este fará um array contendo dois arrays, com três números cada. ([link para script](https://www.minecraft.net/ko-kr))

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

