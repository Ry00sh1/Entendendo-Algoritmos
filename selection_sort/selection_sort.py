#O Selection Sort é um algoritmo de ordenação simples, mas ineficiente para grandes conjuntos de dados. A ideia principal do algoritmo é dividir a lista em duas partes: a sublista dos itens já ordenados, que começa vazia, e a sublista dos itens não ordenados, que ocupa o resto da lista.
#Tempo de execução: O(n)

#Suponha que você tenha uma lista de notas de alunos e deseja ordenar essas notas em ordem crescente para gerar um relatório simples. Dado que a lista é pequena, a eficiência não é uma preocupação crítica.

def selection_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        min_index = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

notas = [85, 92, 78, 88, 95, 90, 80, 90, 78]
print("Notas desordenadas:", notas)
print("Notas ordenadas:", selection_sort(notas))