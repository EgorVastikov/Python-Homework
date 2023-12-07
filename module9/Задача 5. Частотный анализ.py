from collections import Counter
import string

def analyze_letter_frequency(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().lower()

    # Подсчет всех букв
    counts = Counter(c for c in text if c in string.ascii_lowercase)
    total_letters = sum(counts.values())

    if total_letters == 0:
        return

    # Расчет доли каждой буквы
    frequency = {letter: count / total_letters for letter, count in counts.items()}

    sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    with open(output_file, 'w') as file:
        for letter, freq in sorted_frequency:
            file.write(f"{letter} {freq:.3f}\n")

analyze_letter_frequency("text.txt", "analysis.txt")