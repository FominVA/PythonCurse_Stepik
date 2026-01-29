from itertools import pairwise

def max_pair(iterable):
    return max(a+b for a,b in pairwise(iterable))

print(max_pair([1, 8, 2, 4, 3]))