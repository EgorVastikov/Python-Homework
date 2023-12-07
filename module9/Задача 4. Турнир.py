def process_tournament_results(input_file, output_file):
    with open(input_file, 'r') as file:
        k = int(file.readline().strip())
        participants = []

        for line in file:
            surname, name, score = line.split()
            score = int(score)
            if score > k:
                participants.append((surname, name[0], score))

    participants.sort(key=lambda x: -x[2])
    with open(output_file, 'w') as file:
        file.write(f"{len(participants)}\n")
        for i, (surname, initial, score) in enumerate(participants, start=1):
            file.write(f"{i}) {initial}. {surname} {score}\n")

# Вызов функции
process_tournament_results("first_tour.txt", "second_tour.txt")