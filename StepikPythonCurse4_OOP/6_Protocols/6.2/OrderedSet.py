class OrderedSet:

    def __init__(self, iterable=None):
        self.data = []
        self.set = set()
        if iterable is not None:
            for item in iterable:
                if item not in self.set:
                    self.data.append(item)
                    self.set.add(item)

    def add(self, item):
        if item not in self.data:
            self.data.append(item)

    def discard(self, item):
        if item in self.data:
            self.data.remove(item)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.data == other.data
        elif isinstance(other, set):
            return set(self.data) == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))