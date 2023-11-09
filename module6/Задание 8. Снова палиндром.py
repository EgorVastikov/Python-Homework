def forming_palindrome(string):
  count_char = {}
  odd_count = 0

  # Количество вхождений каждой буквы
  for char in string:
    if char in count_char:
      count_char[char] += 1
    else:
      count_char[char] = 1

  # Количество нечётных букв
  for elem in count_char.values():
    if elem % 2 != 0:
      odd_count += 1

  if odd_count > 1:
    return False

  return True


string = input("Введите строку: ")

if forming_palindrome(string):
  print("Можно составить палиндром")
else:
  print("Нельзя составить палиндром")