# 7. Является ли слово палиндромом

string = input("Введите строку: ").lower().replace(" ", "")
print("Палиндром" if string == string[::-1] else "Не палиндром")