with open("zen.txt") as file:
    lines = file.readlines()

lines.reverse()

for line in lines:
    print(line.strip())