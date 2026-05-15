class ModularTuple(tuple):

    def __new__(cls, iterable=(), size=100):
        if iterable:
            transform = tuple(i%size for i in iterable)
        else:
            return ()
        instance = super().__new__(cls, transform)
        return instance

    def __init__(self, iterable, size=100):
        super().__init__()
        self.size = size

    def __mod__(self, n):
        if isinstance(n, int|float):
            return ModularTuple(x % n for x in self)
        return NotImplemented

modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))