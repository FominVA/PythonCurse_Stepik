class PermaDict:

    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = dict(data)

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError("Изменение значения по ключу невозможно")
        if key not in self.data:
            self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]

    def __len__(self):
        return len(self.data)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __iter__(self):
        for key, value in self.data.items():
            yield key, value


permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())
