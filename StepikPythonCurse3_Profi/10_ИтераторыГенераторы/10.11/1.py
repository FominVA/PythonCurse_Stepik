from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

persons = sorted(persons)
s = groupby(sorted(persons, key=lambda tpl: tpl[2]), key=lambda tpl: tpl[2])

for key, group in s:
    names = [i.name for i in group]
    names_str = ', '.join(names)
    print(f'{key}: {names_str}')