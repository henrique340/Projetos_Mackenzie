def bubbleSort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                antigo = list[i]
                list[i] = list[i+1]
                list[i+1] = antigo

list = [54,26,93,17,77,31,44,55,20]
bubbleSort(list)
print(list)