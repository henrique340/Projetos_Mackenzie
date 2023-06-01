def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radixSort(arr):
    max_value = max(arr)

    exp = 1
    while max_value // exp > 0:
        countingSort(arr, exp)
        exp *= 10


# Exemplo de uso:
arr = [66, 45, 75, 90, 802, 24, 2, 175]
radixSort(arr)
print("Array ordenado:")
print(arr)
