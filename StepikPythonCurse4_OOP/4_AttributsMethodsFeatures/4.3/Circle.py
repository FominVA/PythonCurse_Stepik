from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = pi * radius ** 2
        self.diameter = 2 * pi * radius


