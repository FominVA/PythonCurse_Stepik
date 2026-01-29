def add_to_list_in_dict(data, key, element):
    return data.setdefault(key, []).append(element)



data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 7)

print(data)