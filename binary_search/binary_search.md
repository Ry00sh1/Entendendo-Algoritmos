# Binary Search / Busca Binária

Recebendo como entrada uma lista ordenada de `n` elementos, o algoritmo realizará uma busca de um determinado elemento e retornará o índice desse elemento, caso este esteja na lista.

Funcionamento: a busca binária sempre verifica o elemento no meio da lista. Caso o índice retornado (i) não contenha o elemento requisitado (x), o algoritmo efetuará uma comparação entre o elemento no índice e o elemento requisitado até que o mesmo seja encontrado, seguindo os seguintes parâmetros:

1. Se `x < i`: o algoritmo irá efetuar uma nova busca, tendo como faixa de busca `0` (primeiro índice) e `i` (se tornando o último índice, assim criando uma nova lista formada pela menor metade da lista anterior).
2. Se `x > i`: o algoritmo irá efetuar uma nova busca, tendo como faixa de busca `i` (se tornando o primeiro índice) e o `tamanho da lista - 1` (sendo o número total de índices da lista primária).

Caso o algoritmo leia toda a lista e não encontre o elemento, ele retornará `none`.
