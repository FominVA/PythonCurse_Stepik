class ColoredPoint:

    def __init__(self, x: int, y: int, color: tuple=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"
    
    def __pos__(self):
        return ColoredPoint(self.x, self.y)
    
    def __neg__(self):
        return ColoredPoint(-1*self.x, -1*self.y)
    
    def __invert__(self):
        (R, G, B) = self.color
        return ColoredPoint(self.y, self.x, (255-R, 255-G, 255-B))
    
point1 = ColoredPoint(1, 2, (100, 150, 200))
point2 = ~point1

print(repr(point1))
print(repr(point2))