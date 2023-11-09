violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

songs_count = int(input("Сколько песен вы хотите выбрать? "))
total_time = 0

for i in range(songs_count):
    song_name = input(f"Введите название песни номер {i + 1}: ")
    if song_name in violator_songs:
        total_time += violator_songs[song_name]
    else:
        print("Песня не найдена в списке.")

print(f"Общее время звучания песен: {total_time:.2f} минуты")