def bucketSort(array):
    largest = max(array)
    length = len(array)
    size = largest / length

    # Создаем Карзины
    buckets = [[] for i in range(length)]

    # Сортируем
    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    # Сортируем Карзины
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])

    # Выводим
    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


arr = [5, 4, 2, 7, 8, 55, 2, 1, 4, 5, 1, 2]
output = bucketSort(arr)
print(output)