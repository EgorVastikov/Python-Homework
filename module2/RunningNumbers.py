# 6. Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций.

n = int(input("Кол-во элементов в списке: "))
k = int(input("На сколько сдвинуть? "))
arr = []
result = []

for _ in range(n):
    arr.append(int(input("Введите число: ")))

temp = n - k
for i in range(n):
    if temp > n - 1:
        temp = temp - n

    result.append(arr[temp])
    temp += 1


print(f"Сдвинутый список: {result}")