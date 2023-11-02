n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))
circle_people = list(range(1, n + 1))
index = 0

while len(circle_people) != 1:
    print(f"Текущий круг людей: {circle_people}")
    print(f"Начало счёта с номера {circle_people[index % len(circle_people)]}")
    index = (index + k - 1) % len(circle_people)
    print(f"Выбывает человек под номером {circle_people[index]}\n")

    circle_people.remove(circle_people[index])

print(f"Остался человек под номером {circle_people[0]}")