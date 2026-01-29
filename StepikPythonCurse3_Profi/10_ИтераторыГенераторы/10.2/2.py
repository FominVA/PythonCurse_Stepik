def filterfalse(predicate, iterable):
    if predicate is None:
        def inverse_bool(item):
            return not bool(item)
        return filter(inverse_bool, iterable)
    else:
        def inverse_predicate(item):
            return not predicate(item)
        return filter(inverse_predicate, iterable)
    
objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))