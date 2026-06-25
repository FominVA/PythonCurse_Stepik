from math import sqrt

class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __str__(self):
        return f'{', '.join((str(x) for x in self.coords))}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Vector) and len(self.coords) == len(other.coords):
            return self.coords == other.coords
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        if isinstance(other, Vector) and len(self.coords) == len(other.coords):
            new_coords = tuple(a+b for a, b in zip(self.coords, other.coords))
            return Vector(new_coords)
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __mul__(self, other):
        if isinstance(other, Vector) and len(self.coords) == len(other.coords):
            new_coords = sum(a*b for a, b in zip(self.coords, other.coords))
            return new_coords
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __sub__(self, other):
        if isinstance(other, Vector) and len(self.coords) == len(other.coords):
            new_coords = tuple(a-b for a, b in zip(self.coords, other.coords))
            return Vector(new_coords)
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def norm(self):
        return sqrt(sum(x**2 for x in self.coords))

vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector3.norm())
