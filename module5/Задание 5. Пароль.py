import re
def is_password_strong(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if len(re.findall(r'\d', password)) < 3:
        return False

    return True


while True:
    password = input("Придумайте пароль: ")
    if is_password_strong(password):
        print("Пароль надёжный.")
        break
    else:
        print("Пароль не надёжный.")