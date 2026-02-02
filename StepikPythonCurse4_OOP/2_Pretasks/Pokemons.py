from itertools import groupby
from sys import stdin

data = groupby([pokemon.strip() for pokemon in stdin])
for key, value in data:
    print(key, list(value))