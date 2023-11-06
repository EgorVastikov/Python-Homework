def count_uppercase_lowercase(text):
    uppercase, lowercase = 0, 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return uppercase, lowercase

text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)