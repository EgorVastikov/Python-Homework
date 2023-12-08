def validate_data(line):
    parts = line.strip().split()
    if len(parts) != 3:
        raise IndexError("Недостаточно данных")

    name, email, age = parts
    if not name.isalpha():
        raise NameError("Некорректное имя")
    if '@' not in email or '.' not in email:
        raise SyntaxError("Некорректный имейл")
    if not (age.isdigit() and 10 <= int(age) <= 99):
        raise ValueError("Некорректный возраст")

    return line

def process_registrations(file_path):
    with open(file_path, "r", encoding="utf-8") as file, \
         open("registrations_good.log", "w", encoding="utf-8") as good_log, \
         open("registrations_bad.log", "w", encoding="utf-8") as bad_log:

        for line in file:
            try:
                validated_line = validate_data(line)
                good_log.write(validated_line + "\n")
            except (IndexError, NameError, SyntaxError, ValueError) as e:
                bad_log.write(f"{line.strip()} - Ошибка: {e}\n")

process_registrations("registrations.txt")