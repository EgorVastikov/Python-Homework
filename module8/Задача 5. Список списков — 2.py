def expending_list(nested_list):
    exp_list = []
    for element in nested_list:
        if isinstance(element, list):
            # Рекурсивно выпрямляем вложенные списки
            exp_list.extend(expending_list(element))
        else:
            # Добавляем элементы, не являющиеся списками, напрямую
            exp_list.append(element)
    return exp_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(expending_list(nice_list))