count_rollers = int(input("Кол-во роликов: "))
count_people = int(input("Кол-во людей: "))
size_rollers = []
leg_people = []
result = 0

for _ in range(count_rollers):
    size_rollers.append(int(input("Размер роликов: ")))

for _ in range(count_people):
    leg_people.append(int(input("Размер ноги: ")))

for roll in size_rollers:
    for leg in leg_people:
        if roll == leg:
            result += 1
            size_rollers.remove(roll)
            leg_people.remove(roll)

print(f"Наибольшее количество людей, которые могут взять ролики: {result}")