def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        left = [x for x in lista[1:] if x < pivot]
        right = [x for x in lista[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


list = [1, 7, 4, 1, 10, 9, -2]
sorted = quicksort(list)
print(sorted)