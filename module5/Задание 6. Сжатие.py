string = input("Введите строку: ")
current_symbol = string[0]
counter = 1
new_string = ""

for sym in range(1, len(string)):
    if string[sym] == current_symbol:
        counter += 1
    else:
        new_string = "".join([new_string, current_symbol, str(counter)])
        counter = 1
        current_symbol = string[sym]

new_string = "".join([new_string, current_symbol, str(counter)])
print(f"Закодированная строка: {new_string}")