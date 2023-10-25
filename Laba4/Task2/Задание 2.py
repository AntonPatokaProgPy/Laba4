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


def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


quadratic_algo([4, 5, 6, 8])


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
print(permutations([1, 23, 5, 6, 4]))
