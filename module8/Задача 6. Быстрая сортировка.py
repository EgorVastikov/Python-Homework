def help_func(some_list):
    first_list = [elem for elem in some_list if elem < some_list[-1]]
    second_list = [elem for elem in some_list if elem == some_list[-1]]
    third_list = [elem for elem in some_list if elem > some_list[-1]]

    return first_list, second_list, third_list


def quick_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list

    l1, l2, l3 = help_func(sort_list)
    result = []

    result.extend(quick_sort(l1))
    result.extend(l2)
    result.extend(quick_sort(l3))

    return result


sort_list = [5, 8, 9, 4, 2, 9, 1, 8]
print(quick_sort(sort_list))