# 5. Задание 5. Контейнеры

count_containers = int(input("Количество контейнеров: "))
containers = []

# Заполняем склад контейнерами
while count_containers != 0:
    value = int(input("Масса контейнера: "))

    if value > 200:
        print("Вес не может быть больше 200")
        continue
    else:
        count_containers -= 1
        containers.append(value)

new_container = int(input("Введите вес нового контейнера: "))
while new_container > 200:
    print("Вес не может быть больше 200")
    new_container = int(input("Введите вес нового контейнера: "))

# Позиция нового контейнера
for i in range(len(containers)):
    if new_container > containers[i]:
        print(f"Позиция нового контейнера: {i + 1}")
        break
else:
    print(f"Позиция нового контейнера: {len(containers) + 1}")