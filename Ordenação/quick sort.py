def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]  #adota o pivot como o primeiro elemento da lista
        left = [x for x in lista[1:] if x < pivot]  #cria uma lista para os elementos menores que o pivot
        right = [x for x in lista[1:] if x >= pivot]  # cria uma lista para os elementos maiores que o pivot
        return quicksort(left) + [pivot] + quicksort(right)   #Junta as listas


list = [1, 7, 4, 1, 10, 9, -2]
sorted = quicksort(list)
print(sorted)