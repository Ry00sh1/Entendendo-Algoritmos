'''Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.'''

def busca_binaria(lista, elemento): #função cotendo o algoritmo de busca binária
    primeiro = 0
    ultimo = len(lista)-1
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == elemento: #elemento encontrado
            print(f"ÍNDICE FINAL = {meio}")
            return print(f"ELEMENTO = {lista[meio]}")
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
                print(f"ÍNDICE = {meio}")
            else:
                primeiro = meio + 1
                print(f"ÍNDICE = {meio}")
    return False

lista = [ x for x in range(1, 101)] #gera uma lista contendo inteiros de 1 a 100
elemento = 8 #elemento a ser buscado

busca_binaria(lista,elemento) #chamada da função