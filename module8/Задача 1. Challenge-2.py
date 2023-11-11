def print_nums(num, index):
    print(index)
    if num == index:
        return
    return print_nums(num, index + 1)


number = int(input("Введите число: "))
index = 1
print_nums(number, 1)