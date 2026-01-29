from itertools import cycle
from string import ascii_uppercase

def alnum_sequence():
    for i in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from i

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))