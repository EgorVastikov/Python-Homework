# 3. Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.

count_video_cards = int(input("Кол-во видеокарт: "))
video_cards = []

for i in range(count_video_cards):
    vc = int(input(f"Видеокарта {i + 1}: "))
    video_cards.append(vc)

maximum = max(video_cards)

while maximum in video_cards:
    video_cards.remove(maximum)

print(video_cards)