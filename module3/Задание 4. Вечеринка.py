guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек")
    name_guest = input("Имя гостя: ")
    move = input("Гость пришёл или ушёл: ").lower()

    if move == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    elif move == "пришёл":
        if len(guests) < 6:
            guests.append(name_guest)
            print(f"Привет, {name_guest}!\n")
        else:
            print(f"Прости, {name_guest}, но мест нет.\n")
    elif move == "ушёл":
        guests.remove(name_guest)
        print(f"Пока, {name_guest}!\n")
    else:
        print(f"Команды \"{move}\" нет попробуйте ещё раз\n")