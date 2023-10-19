# 9 Напишите программу, которая считывает целые числа из списка и выводит из него только чётные в обратном порядке.
# Создавать дополнительные списки нельзя.

list_nums = [1, 2, 3, 4, 5, 6, 5, 6, 7, 2]

# Разворачиваем список
for i in range(len(list_nums)):
    for j in range(len(list_nums) - i - 1):
        if list_nums[j] < list_nums[j + 1]:
            list_nums[j], list_nums[j + 1] = list_nums[j + 1], list_nums[j]

# Удаление нечётных элементов
for i in range(len(list_nums) - 1, -1, -1):
    if list_nums[i] % 2 != 0:
        list_nums.pop(i)

print(list_nums)