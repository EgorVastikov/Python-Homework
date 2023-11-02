def merge_sorted_lists(l1, l2):
    l1.extend(l2)
    set_lists = set(l1)
    new_list = sorted(list(set_lists))
    return new_list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)