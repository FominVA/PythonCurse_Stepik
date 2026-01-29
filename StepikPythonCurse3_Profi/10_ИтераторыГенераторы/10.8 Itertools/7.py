from itertools import dropwhile

def first_true(iterable, predicate):
    i = list(filter(predicate, iterable))
    if i == []:
        return None
    else:
        return i[0]

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))