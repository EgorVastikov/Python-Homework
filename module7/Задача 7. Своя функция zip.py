def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]

    min_length = min(len(it) for it in iterables)

    for _ in range(min_length):
        yield tuple(next(it) for it in iterators)


string = "abcd"
numbers = (10, 20, 30, 40)

pairs_generator = my_zip(string, numbers)
print(pairs_generator)

for pair in pairs_generator:
    print(pair)
