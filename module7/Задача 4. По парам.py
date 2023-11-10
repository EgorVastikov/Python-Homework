import random as rnd

random_list = [rnd.randint(0, 10) for _ in range(10)]
select_list = [(random_list[i], random_list[i + 1]) for i in range(9)]

print(random_list)
print(select_list)