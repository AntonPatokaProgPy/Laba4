def merge_sort(nums):
    if len(nums) > 1:# делаем в if чтобы не было саиска в 1 и 0
        mid = len(nums)//2 #Разделяем список надвое,мы будем использовать целочисленное деление, чтобы в итоге получить целый индекс
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)#Cортируем
        i = j = k = 0# 3 индекса
        while i < len(left) and j < len(right):#Если число из списка left меньше, чем число из списка right, мы вставляем его в nums на позицию k, после чего увеличиваем индекс i на единицу. Если число из списка right меньше или равно числу из списка left, тогда оно отправляется в nums, а мы увеличиваем на единицу индекс j.
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i < len(left): #Перебираем остатки
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1
nums = [5, 2, 3, 6, 84, 9, 8]#Проверяем
merge_sort(nums)
print(nums)