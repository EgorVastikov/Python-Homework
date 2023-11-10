import math
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def crypto(obj):
    return [elem for i, elem in enumerate(obj) if is_prime(i)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))