import random

def request_numbers_and_write_to_file():
    sum_of_numbers = 0
    while sum_of_numbers < 777:
        try:
            if random.randint(1, 13) == 1:
                raise Exception("Случайное исключение")

            number = int(input("Введите число: "))

            with open("out_file.txt", "a", encoding="utf-8") as file:
                file.write(f"{number}\n")

            sum_of_numbers += number

        except Exception as e:
            print(f"Программа завершилась с исключением: {e}")
            break

request_numbers_and_write_to_file()