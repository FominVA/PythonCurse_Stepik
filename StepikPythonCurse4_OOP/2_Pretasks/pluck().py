
def pluck(data, path, default=None):
    parts = path.split('.')
    for i in parts:
        if isinstance(data, dict):
            data = data.get(i, default)
        else:
            return default
    return data
    

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'x'))