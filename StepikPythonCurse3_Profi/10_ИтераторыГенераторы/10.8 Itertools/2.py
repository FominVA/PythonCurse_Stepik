from itertools import accumulate

def factorials(n):
    g = range(1, n+1)
    f = lambda x, y: x*y
    yield from accumulate(g, func=f)

numbers = factorials(6)

print(*numbers)