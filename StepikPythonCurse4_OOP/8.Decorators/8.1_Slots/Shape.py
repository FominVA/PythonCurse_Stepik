class Shape:

    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        return NotImplemented

shape = Shape('square', 'LemonChiffon', 50)
not_supported = [[1, 2], True, (1, 2, 3, 4), 'beegeek', {'name': 'Grace Hopper'}, {18, 22}]

for item in not_supported:
    print(shape == item)
    print(item == shape)