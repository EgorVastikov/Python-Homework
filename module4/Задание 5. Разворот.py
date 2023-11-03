string = input("Введиете строку: ")

first_h = string.find('h')
last_h = string.rfind('h')
reverse_string = string[first_h + 1:last_h][::-1]

print(reverse_string)