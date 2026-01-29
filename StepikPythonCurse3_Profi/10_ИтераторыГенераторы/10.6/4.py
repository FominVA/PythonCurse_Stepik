def all_together(*args):
    for el in args:
        yield from el

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))\