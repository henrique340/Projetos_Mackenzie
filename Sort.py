# Quick Sort
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

# Merge Sort
def merge(left, right):
	resultado = []
	i, j = 0, 0
	while i < len(left) and j<len(right):
		if left[i] < right[j]:
			resultado.append(left[i])
			i+= 1
		else:
			resultado.append(right[j])
			j += 1
	resultado += left[i:]
	resultado += right[:j]
	return resultado

def MergeSort(lista):
	if len(lista) <= 1:
		return lista
	mid = int(len(lista)/2)
	left = MergeSort(lista[:mid])
	right = MergeSort(lista[mid:])
	return merge(left, right)

myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]

