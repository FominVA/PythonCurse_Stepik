class CyclicList:

    def __init__(self, iterable):
        self.data = list(iterable)

    def append(self, item):
        return self.data.append(item)

    def pop(self, index=-1):
        if not isinstance(index, int):
            index = -1
        return self.data.pop(index)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        index = index % len(self.data)
        return self.data[index]

    def __iter__(self):
        for index in range(len(self.data)):
            yield self.data[index % len(self.data)]
        # После прохода по всем элементам — начинаем сначала
        while True:
            for index in range(len(self.data)):
                yield self.data[index]

cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')




