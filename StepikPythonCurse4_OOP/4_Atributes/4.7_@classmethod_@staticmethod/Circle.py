class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle(self):
        return self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

circle1 = Circle(51.5)
circle2 = Circle.from_diameter(45)