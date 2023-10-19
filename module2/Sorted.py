# 8. Сортировка

def bubble_sort(list_nums):
    for _ in range(len(list_nums)):
        for i in range(len(list_nums) - 1):
            if list_nums[i] > list_nums[i+1]:
                list_nums[i], list_nums[i+1] = list_nums[i+1], list_nums[i]

    return list_nums


list_nums = [1, 4, -3, 0, 10]
print(bubble_sort(list_nums))