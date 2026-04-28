class HistoryDict:

    def __init__(self, data=None):
        self.data = dict(data) if data else {}
        self.history_data = {key: [value] for key, value in self.data.items()}

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def history(self, key):
         return list(self.history_data.get(key, []))

    def all_history(self):
        return {key: list(self.history_data[key]) for key in self.data}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key] = value
            self.history_data[key].append(value)
        else:
            self.data[key] = value
            self.history_data[key] = [value]

    def __delitem__(self, key):
        del self.data[key]
        del self.history_data[key]

    def __iter__(self):
        return iter(self.data)

historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())