def countingSort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr


# Exemplo de uso:
arr = [4, 2, 1, 4, 3, 2, 1, 4]
sorted_arr = countingSort(arr)
print("Array ordenado:")
print(sorted_arr)
