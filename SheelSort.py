def ShellSort(lista):
    inter = len(lista) // 2
    while inter >= 1:
        i = 0
        while i < inter:
            j = i + inter
            while j < len(lista):
                if lista[j] < lista[j-inter]:
                    lista[j], lista[j-inter] = lista[j-inter], lista[j]
                j = j + inter
            i = i + 1
        inter = inter // 2

array = [8, 9, 2, 0, 7, 1, 6, 4, 3, 5]
ShellSort(array)
print(array)