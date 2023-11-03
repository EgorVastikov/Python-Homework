n = int(input("Введите длину списка: "))
l1 = [(1 if num % 2 == 0 else num % 5) for num in range(n)]

print(l1)