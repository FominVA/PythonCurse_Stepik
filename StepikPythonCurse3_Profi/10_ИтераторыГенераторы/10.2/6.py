
def get_min_max(iterable):
    try:
        iterator = iter(iterable)
        try:
            first_element = next(iterator)
        except StopIteration:
            return None
        min_value = first_element
        max_value = first_element
        for el in iterator:
            if el < min_value:
                min_value = el
            if el > max_value:
                max_value = el
        return (min_value, max_value)
    except TypeError:
        return None

iterable = iter(range(10))

print(get_min_max(iterable))

