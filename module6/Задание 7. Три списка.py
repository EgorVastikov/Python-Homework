array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

set1 = set(array_1)
set2 = set(array_2)
set3 = set(array_3)

# найти элементы, которые есть в каждом списке;
result_list = []
for elem in array_1:
    if elem in array_2 and elem in array_3:
        result_list.append(elem)

print(f"без использования множеств: {result_list}")
print(f"с использованием множеств: {list(set1.intersection(set2).intersection(set3))}")
result_list.clear()

# найти элементы из первого списка, которых нет во втором и третьем списках
for elem in array_1:
    if not (elem in array_2 or elem in array_3):
        result_list.append(elem)

print(f"без использования множеств: {result_list}")
print(f"с использования множеств: {list(set1.difference(set2, set3))}")