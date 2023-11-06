# cdabcdab
def shift(s1, s2):
    if len(s1) != len(s2):
        return "Нельзя получить строку путём сдвига"

    # Получаем строку в которой содержатся все циклические сдвиги строки
    double_s2 = s2 + s2
    position = double_s2.find(s1)

    if position != -1:
        return f"Первая строка получается из второй со сдвигом {position}."
    else:
        return "Первую строку нельзя получить из второй с помощью циклического сдвига."


string1 = "abcd"
string2 = "cdab"
print(shift(string1, string2))