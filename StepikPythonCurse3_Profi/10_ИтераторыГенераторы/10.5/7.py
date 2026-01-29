def flatten(nested_list):
    for el in nested_list:
        if isinstance(el, list):
            yield from flatten(el)
        else:
            yield el
    
generator = flatten([12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]])

print(*generator)