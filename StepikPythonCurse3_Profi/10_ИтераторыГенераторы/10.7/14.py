def around(iterable):
    previous = None
    if type(iterable) != list:
        iterable = [i for i in iterable]
    for i in range(len(iterable)):
        try:
            yield (previous, iterable[i], iterable[i+1])
            previous = iterable[i]
        except:
            yield (iterable[i-1], iterable[i],None)  

iterator = iter('hey')

print(*around(iterator))

