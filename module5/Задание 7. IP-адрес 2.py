def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        if not 0 <= int(part) <= 255:
            return False

    return True

ip = input("Введите IP: ")
if is_valid_ip(ip):
    print("Введённая строка является правильным IP-адресом.")
else:
    print("Введённая строка не является правильным IP-адресом.")