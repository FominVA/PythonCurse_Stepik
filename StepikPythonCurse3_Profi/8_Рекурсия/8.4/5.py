def dict_travel(nested_dicts, prefix=''):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            dict_travel(v, prefix+k+'.')
        else:
            print(f'{prefix}{k}: {v}')

data = {'a': 'dsafsd', 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)