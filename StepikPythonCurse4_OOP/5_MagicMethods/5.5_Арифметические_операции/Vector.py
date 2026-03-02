class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, value):
        if isinstance(value, Vector):
            return self.x == value.x and self.y == value.y
        elif isinstance(value, tuple) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int|float):
            return Vector(self.x*n, self.y*n)
        return NotImplemented
    
    def __rmul__(self, n):
        if isinstance(n, int|float):
            return Vector(n*self.x, n*self.y)
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, int|float):
            return Vector(self.x/n, self.y/n)
        return NotImplemented