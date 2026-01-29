from itertools import zip_longest

def roundrobin(*args):
    it = list(map(iter, args))
    slices = zip_longest(*it, fillvalue='n')
    for tup in slices: 
        for el in tup:
            if el != 'n':
                yield el

numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))
