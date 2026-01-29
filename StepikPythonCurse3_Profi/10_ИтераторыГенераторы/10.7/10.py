def unique(iterable):
    dct = {}
    for num in iterable:
        dct[num] = 0
    yield from dct


numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))