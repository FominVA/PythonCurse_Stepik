class Row:

    def __init__(self, **kwargs):
        self.__dict__['_data'] = kwargs

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError('Установка нового атрибута невозможна')
        else:
            raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        return f"Row({self._data})"

    def __eq__(self, other):
        if isinstance(other, Row):
            return self._data == other._data
        return NotImplemented

    def __hash__(self):
        return hash(frozenset(self._data.items()))

row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))
