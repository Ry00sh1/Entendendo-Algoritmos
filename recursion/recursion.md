# Recursion / Recursão
**Algoritmo de resolução de problemas**<br>
**Tempo de execução: Depende do problema (pode variar de O(log n) a O(n!), por exemplo)**

"Os loops podem melhorar o desempenho do seu programa. A recursão melhora o desempenho do seu programador." - Leigh Caldwell
A recursão é uma técnica de resolução de problemas onde a solução de um problema depende de soluções de instâncias menores do mesmo problema. Um algoritmo recursivo chama a si mesmo repetidamente até que uma condição de base seja satisfeita, evitando chamadas adicionais. Um dos exemplos mais clássicos é o cálculo do fatorial de um número ou a sequência de Fibonacci.

## Vantagens e Desvantagens
### Vantagens
- Simplicidade: Para muitos problemas, a recursão oferece uma maneira simples e intuitiva de expressar a solução.
- Adequada para problemas divididos em subproblemas: Usada em problemas onde a solução pode ser dividida em subproblemas menores de forma natural, como árvores e grafos.
### Desvantagens
- Consumo de memória: Pode utilizar mais memória devido ao empilhamento de chamadas de função (stack).
- Performance: Pode ser ineficiente se não for usada com técnicas de otimização, como memoization ou tail recursion.
- Dificuldade de depuração: Algoritmos recursivos podem ser mais difíceis de entender e depurar do que suas contrapartes iterativas.