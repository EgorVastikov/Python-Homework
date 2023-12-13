from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

# 1. Каждое число из списка floats возводится в третью степень и округляется до трех знаков после запятой
cubed_and_rounded = list(map(lambda num: round(num ** 3, 3), floats))

# 2. Из списка names берутся только имена минимум из пяти букв
long_names = list(filter(lambda name: len(name) >= 5, names))

# 3. Из списка numbers берется произведение всех чисел
product_of_all_numbers = reduce(lambda x, y: x * y, numbers)

print(cubed_and_rounded)
print(long_names)
print(product_of_all_numbers)