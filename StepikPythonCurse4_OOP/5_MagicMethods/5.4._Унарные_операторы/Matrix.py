class Matrix:

    def __init__(self, rows: int, cols: int, value: int=0):
        self.rows = rows
        self.cols = cols
    

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