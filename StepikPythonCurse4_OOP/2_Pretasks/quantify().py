numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quantify(iterable, predicate):
    return len(list(filter(predicate, iterable)))

print(quantify(numbers, lambda x: x > 1))