from itertools import pairwise

def is_rising(iterable):
    return all(a < b for a, b in pairwise(iterable))
    
iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))