def intersperse(iterable, delimiter):
    iterator_list = []
    for el in iterable:
        iterator_list.append(el)
        iterator_list.append(delimiter)
    iterator_list = iterator_list[:-1]
    iterator = iter(iterator_list)
    for item in iterator:
        yield item