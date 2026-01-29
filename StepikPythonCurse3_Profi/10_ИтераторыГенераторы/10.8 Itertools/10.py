
def first_largest(iterable, number):
    for i, j in enumerate(iterable):
        if j > number:
            return i
            break
    return -1

numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))