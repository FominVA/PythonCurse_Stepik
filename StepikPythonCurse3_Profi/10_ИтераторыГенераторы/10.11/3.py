from itertools import groupby

#hi never here my blue

l = groupby(sorted(input().split(), key=lambda x: len(x)), key=len)

for key, value in l:
    print(f'{key} -> {", ".join(sorted(value))}')