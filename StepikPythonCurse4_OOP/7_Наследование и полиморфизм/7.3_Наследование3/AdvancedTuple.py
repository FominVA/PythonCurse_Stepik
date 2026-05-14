class AdvancedTuple(tuple):

    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self)+tuple(other))
        return NotImplemented

    def __radd__(self, other):
        # Сложение, когда AdvancedTuple находится справа (iterable + AdvancedTuple)
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented

advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))