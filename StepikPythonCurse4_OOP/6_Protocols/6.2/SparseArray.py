class SparseArray:
    def __init__(self, default):
        self.default = default
        self.data = {}

    def __getitem__(self, index):
        return self.data.get(index, self.default)

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.default)

array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])