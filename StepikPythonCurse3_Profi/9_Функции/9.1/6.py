def custom_isinstance(objects, typeinfo):
    return len([el for el in objects if isinstance(el, typeinfo)])

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))