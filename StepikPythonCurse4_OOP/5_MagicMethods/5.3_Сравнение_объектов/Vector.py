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
    

    
vectors = [Vector(196, 21), Vector(102, 82), Vector(91, 28), Vector(137, 128), Vector(97, 69), Vector(79, 29), Vector(93, 62), Vector(85, 58), Vector(46, 176), Vector(84, 197)]
pairs = [(26, 86), (177, 150), (144, 175), (137, 128), (110, 196), (79, 29), (93, 62), (36, 158), (180, 24), (84, 167)]

for vector, pair in zip(vectors, pairs):
    print(vector == pair, vector != pair)