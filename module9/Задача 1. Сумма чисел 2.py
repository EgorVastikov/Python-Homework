total = 0
with open('numbers.txt') as file:
    for line in file:
        for num in line:
            if num.isdigit():
                total += int(num)

print(total)