class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.items = iter(data.items())

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.items)


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)