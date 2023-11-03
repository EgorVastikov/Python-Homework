text = input("Введите текст: ")
vowel_letters = ["а", "у", "е", "ы", "о", "э", "я", "и", "ю", "ё"]
vowel_in_text = [letter for letter in text if letter in vowel_letters]

print(f"Список гласных букв: {vowel_in_text}")
print(f"Длина списка: {len(vowel_in_text)}")