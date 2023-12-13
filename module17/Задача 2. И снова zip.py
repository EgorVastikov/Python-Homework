letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = [(letters[i], numbers[i]) for i in range(min(len(letters), len(numbers)))]
print(results)