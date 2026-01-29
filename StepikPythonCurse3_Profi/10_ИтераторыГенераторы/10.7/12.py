def with_previous(iterable):
    previous = None
    for current in iterable:
        t = (current, previous)
        previous = current
        yield t


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))