class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def get_length(self):
        return self._length

    def set_length(self, length):
        if isinstance(length, int) and length >= 0:
            self._length = length
        else:
            raise ValueError('Неккоректная длина')
        
    length = property(get_length, set_length)

    def get_width(self):
        return self._width

    def set_width(self, width):
        if isinstance(width, int) and width >= 0:
            self._width = width
        else:
            raise ValueError('Неккоректная ширина')
    
    width = property(get_width, set_width)

    def perimeter(self):
        return 2*(self._length+self._width)
    
    perimeter = property(perimeter)

    def area(self):
        return self._length*self._width
    
    area = property(area)

rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)