# Quick Sort

# Função para achar a posição de partida
def partition(array, low, high):
	# escolhe o elemento da direita como pivot
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


def mergeSort(arr):
	if len(arr) > 1:

		# Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
		mid = len(arr) // 2
		sub_array1 = arr[:mid]
		sub_array2 = arr[mid:]

		# Sort the two halves
		mergeSort(sub_array1)
		mergeSort(sub_array2)

		# Initial values for pointers that we use to keep track of where we are in each array
		i = j = k = 0

		# Until we reach the end of either start or end, pick larger among
		# elements start and end and place them in the correct position in the sorted array
		while i < len(sub_array1) and j < len(sub_array2):
			if sub_array1[i] < sub_array2[j]:
				arr[k] = sub_array1[i]
				i += 1
			else:
				arr[k] = sub_array2[j]
				j += 1
			k += 1

		# When all elements are traversed in either arr1 or arr2,
		# pick up the remaining elements and put in sorted array
		while i < len(sub_array1):
			arr[k] = sub_array1[i]
			i += 1
			k += 1

		while j < len(sub_array2):
			arr[k] = sub_array2[j]
			j += 1
			k += 1


arr = [10, 9, 2, 4, 6, 13]
mergeSort(arr)
print(arr)
