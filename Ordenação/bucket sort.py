def bucketSort(array):
    bucket = []

    # Criar buckets vazios
    for i in range(len(array)):
        bucket.append([])

    # Inserir elementos no bucket
    for item in array:
        index = int(10 * item)
        bucket[index].append(item)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))