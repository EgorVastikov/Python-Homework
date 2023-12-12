class SquaresIterator:
    def __init__(self, max):
        self.max = max
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = self.n ** 2
        self.n += 1
        return result


def squares_generator(max):
    n = 1
    while n <= max:
        yield n ** 2
        n += 1


def squares_expression(max):
    return (n ** 2 for n in range(1, max + 1))


N = 5

print("Класс-итератор:")
for square in SquaresIterator(N):
    print(square)

print("\nФункция-генератор:")
for square in squares_generator(N):
    print(square)

print("\nГенераторное выражение:")
for square in squares_expression(N):
    print(square)
