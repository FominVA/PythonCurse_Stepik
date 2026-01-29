from itertools import chain

def sum_of_digits(iterable):
    s = chain.from_iterable(map(str, iterable))
    return sum(map(int, s))

print(sum_of_digits([13, 20, 41, 2, 2, 5]))