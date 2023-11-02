def make_symmetric(sequence):
    for i in range(len(sequence)):
        if sequence[i:] == sequence[i:][::-1]:
            return sequence[:i][::-1]
    return []


n = int(input("Кол-во чисел: "))
seq = []
for _ in range(n):
    seq.append(int(input("Введите число: ")))

to_add = make_symmetric(seq)

print("Нужно приписать чисел:", len(to_add))
print("Сами числа:", to_add)