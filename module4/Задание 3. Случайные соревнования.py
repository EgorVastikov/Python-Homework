import random

first_group = [round(random.uniform(5,10), 2) for _ in range(20)]
second_group = [round(random.uniform(5,10), 2) for _ in range(20)]
winners = [(a if a > b else b) for a, b in zip(first_group, second_group)]

print(f"Первая команда: {first_group}")
print(f"Вторая команда: {second_group}")
print(f"Победители тура: {winners}")