from collections import Counter

def analyze_letter_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    letter_counts = Counter(c for c in text if c.isalpha())

    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_letters:
        print(f"{letter}: {count}")

file_path = 'War_and_peace.txt'
analyze_letter_frequency(file_path)