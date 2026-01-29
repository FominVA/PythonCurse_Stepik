def get_all_values(nested_dicts, key):
    m = []
    if key in nested_dicts:
        m += [nested_dicts[key]]

    for v in nested_dicts.values():
        if isinstance(v, dict):
            value = get_all_values(v, key)
            if value is not None:
                m += value
    return set(m)

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))