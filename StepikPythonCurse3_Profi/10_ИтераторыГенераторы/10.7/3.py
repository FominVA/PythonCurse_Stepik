import itertools

def filter_names(names: list, ignore_char: str, max_names: int):
    g = (name for name in names if name[0] != 'D' and name.isalpha() == True)
    yield from itertools.islice(g, max_names)


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))