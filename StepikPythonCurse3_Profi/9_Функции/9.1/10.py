def zip_longest(*args, fill=None):
    max_len = max([len(i) for i in args])
    result = []
    for i in range(max_len):
        tuples = []
        for lst in args:
            if i < len(lst):
                 tuples.append(lst[i])
            else:
                tuples.append(fill)
        result.append(tuple(tuples))
    return result

print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))