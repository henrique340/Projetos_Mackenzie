def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Construir um heap máximo
    for i in range(n // 2 - 1, -1, -1):  # i -> 2, 1, 0 (nó pai)
        heapify(arr, n, i)

    # Extrair elementos um por um
    for i in range(n - 1, 0, -1):    # i -> 5, 4, 3, 2, 1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)
