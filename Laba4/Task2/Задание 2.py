def algorithm(n):  # 3n
    for i in range(3 * n):
        print(i)


def quick_sort(arr):  # nlogn
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


# def permutations(arr):  # n!
#     if len(arr) <= 1:
#         return [arr]
#     else:
#         result = []
#         for i in range(len(arr)):
#             rest = arr[:i] + arr[i + 1:]
#     for p in permutations(rest):
#         result.append([arr[i]] + p)
#         return result
def generate_permutations(arr):
    if len(arr) == 0:
        return [[]]  # базовый случай, возвращаем пустой список

    permutations = []  # результирующий список перестановок

    for i in range(len(arr)):
        element = arr[i]
        remaining_elements = arr[:i] + arr[i + 1:]  # удаляем текущий элемент из массива
        for permutation in generate_permutations(remaining_elements):
            permutations.append(
                [element] + permutation)  # объединяем текущий элемент с перестановкой оставшихся элементов

    return permutations


# пример использования
arr = [1, 2, 3]
permutations = generate_permutations(arr)
print(permutations)


def algorithm2(n):  # n3
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


def algorithm3(n5):
    for i in range(3):
        low = 0
        high = n5 - 1
        while low <= high:
            mid = (low + high) // 2
            if algorithm(n5):
                high = mid - 1
            else:
                low = mid + 1


print(quick_sort([1, 23, 5, 6, 4]))
print(generate_permutations([1, 23, 5, 6, 4]))
