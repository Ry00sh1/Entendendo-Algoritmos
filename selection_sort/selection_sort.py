#Suponha que você tenha uma lista de notas de alunos e deseja ordenar essas notas em ordem crescente para gerar um relatório simples. Dado que a lista é pequena, a eficiência não é uma preocupação crítica.

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

notas = [85, 92, 78, 88, 95, 90, 80, 90, 78]
print("Notas desordenadas:", notas)
print("Notas ordenadas:", selection_sort(notas))