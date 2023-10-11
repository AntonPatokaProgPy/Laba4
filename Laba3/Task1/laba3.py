import timeit


# Быстрая сортировка рекурсивым методом
def quick_sort(s: list) -> list:
    if len(s) <= 1:
        return s
    center = s[0]
    left = [i for i in s if i < center]
    middle = [i for i in s if i == center]
    right = [i for i in s if i > center]
    return quick_sort(left) + middle + quick_sort(right)


# Сортировка сортировки расческой
def comb_sort(s: list) -> list:
    step = len(s) - 1
    while step > 0:
        for i in range(0, len(s) - step):
            if (s[i] > s[i + step]):
                s[i], s[i + step] = s[i + step], s[i]
        step = int(step // 1.25)
    return s


x = [3, -99, 10, 2]
time = timeit.timeit(stmt='quick_sort(s=x)', globals=globals())
time1 = timeit.timeit(stmt='comb_sort(s=x)', globals=globals())
print(time)
print(time1)
