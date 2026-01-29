from copy import deepcopy

def pairwise(iterable):
    it = list(deepcopy(iterable))
    next_it = list(iterable)[1:]
    next_it.append(None)
    for it1, it2 in zip(it, next_it):
        yield (it1, it2)

iterator = iter('stepik')

print(*pairwise(iterator))