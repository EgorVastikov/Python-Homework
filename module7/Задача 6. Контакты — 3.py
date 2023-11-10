def main():
    contacts = {}

    while True:
        action = input("Введите номер действия: \n1. Добавить контакт\n2. Найти человека\n")

        if action == "1":
            full_name = input("Введите имя и фамилию нового контакта (через пробел): ").strip().split()
            if len(full_name) != 2:
                print("Неверный формат ввода. Пожалуйста, введите имя и фамилию.")
                continue

            full_name = tuple(full_name)
            if full_name in contacts:
                print("Такой человек уже есть в контактах.")
            else:
                phone_number = input("Введите номер телефона: ")
                contacts[full_name] = phone_number
                print("Контакт добавлен.")

            print("Текущий словарь контактов:", contacts)

        elif action == "2":
            search_surname = input("Введите фамилию для поиска: ").lower()
            found = False

            for (first_name, surname), phone_number in contacts.items():
                if surname.lower() == search_surname:
                    print(f"{first_name} {surname} {phone_number}")
                    found = True

            if not found:
                print("Контакт с такой фамилией не найден.")

        else:
            print("Неверный выбор. Введите 1 или 2.")


main()