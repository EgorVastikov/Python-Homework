def count_characters(text):
    # Подсчет частоты каждого символа в строке
    frequency_dict = {}
    for char in text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

def invert_dictionary(original_dict):
    # Инвертирование словаря
    inverted_dict = {}
    for char, frequency in original_dict.items():
        if frequency in inverted_dict:
            inverted_dict[frequency].append(char)
        else:
            inverted_dict[frequency] = [char]
    return inverted_dict


text = "здесь что-то написано"

frequency_dict = count_characters(text)
inverted_frequency_dict = invert_dictionary(frequency_dict)

print("Инвертированный словарь частот:")
for key, value in inverted_frequency_dict.items():
    print(key, value)