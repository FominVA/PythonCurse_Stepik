from itertools import zip_longest

def grouper(iterable, n):
    args = [iter(iterable)]*n
    return zip_longest(*args)

numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))