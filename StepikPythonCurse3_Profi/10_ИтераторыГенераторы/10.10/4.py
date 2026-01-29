from itertools import tee, chain

def ncycles(iterable, times):
    result = chain.from_iterable(tee(iterable))
    return result
    

print(*ncycles([1, 2, 3, 4], 3))
