def count_unique_characters(s):
    s_lower = s.lower()
    unique_chars = filter(lambda char: s_lower.count(char) == 1, set(s_lower))
    return len(list(unique_chars))


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)