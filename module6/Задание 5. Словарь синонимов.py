word_count = int(input("Введите количество пар слов: "))
dictionary_synonyms = {}

for word in range(1, word_count + 1):
    words = input(f"{word}-я пара (вводитие пару слов через - (тире) без пробелов): ").split('-')
    dictionary_synonyms[words[0].title()] = words[1].title()
    dictionary_synonyms[words[1].title()] = words[0].title()

while True:
    word = input("Введите слово: ").title()
    if word in dictionary_synonyms:
        print(f"Синоним: {dictionary_synonyms[word]}")
        break
    else:
        print("Такого слова в словаре нет.")