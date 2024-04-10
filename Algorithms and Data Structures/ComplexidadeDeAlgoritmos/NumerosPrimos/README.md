# Números Primos

### Algoritmo de Fermat para números primos

O algoritmo de Fermat parte do princípio que todo número não primo pode ser representado pelo produto de 2 números diferentes do próprio número. Qualquer número que não se encaixe nessa regra é considerado primo.

Considerando um número N que possua uma raiz quadrada exata, os números x e Y que multiplicados representam N podem ser:
- Dois números iguais a raiz quadrada de N;
- Dois números diferentes onde x < sqrt(N) e y > sqrt(N).

Logo, para avaliarmos se um número é primo, podemos validar se o número não é primo e negar essa informação. 

Seguindo as regras explicadas anteriormente, basta procurarmos um divisor com resto 0 para N entre [2; sqrt(N)];

Logo, o algoritmo de Fermat possui complexidade O(sqrt(n)) em seu pior caso. 
