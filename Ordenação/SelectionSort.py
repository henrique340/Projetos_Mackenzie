def SelectionSort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista

list = [1, 7, 4, 1, 10, 9, -2]
sorted = SelectionSort(list)
print(sorted)