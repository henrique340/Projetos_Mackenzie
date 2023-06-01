def InsertionSort(lista):
    for i in range(len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = key
    return lista

arr = [12, 11, 13, 5, 6]
sorted = InsertionSort(arr)
print(sorted)