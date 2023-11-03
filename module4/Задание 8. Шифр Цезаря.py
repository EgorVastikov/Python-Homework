alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_upper = alphabet.upper()

def cipher_text(text, shift):
    encrypted_text = []

    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text.append(alphabet[index])
        elif char in alphabet_upper:
            index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
            encrypted_text.append(alphabet_upper[index])
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


text = input("Введите текст: ")
shift = int(input("Введите величину сдвига: "))

print(f"Зашифрованное сообщение: {cipher_text(text, shift)}")