from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

def alive(persons):
    for pers in persons:
        if pers.death == 0:
            yield pers

def sex(iterable):
    for pers in iterable:
        if pers.sex == 'male':
            yield pers

def nation(iterable):
    for pers in iterable:
        if pers.nationality == 'Swedish':
            yield pers            

def youngest(iterable):
    y = list(filter(lambda p: p.birth, iterable))[-1]
    yield y
#alive_p = (pers for pers in persons if pers.death == 0 and pers.nationality == 'Swedish' and pers.sex == 'male')

def name(iterable):
    for pers in iterable:
        result = pers.name
    yield result

print(*name(youngest(alive((nation((sex(persons))))))))