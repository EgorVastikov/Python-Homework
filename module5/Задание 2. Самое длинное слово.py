text = input("Введите строку: ").split()
maximum = 0

for word in text:
    if len(word) > maximum:
        maximum = len(word)

for word in text:
    if len(word) == maximum:
        print("Самое длинное слово:", word)
        break

print("Длина этого слова:", maximum)