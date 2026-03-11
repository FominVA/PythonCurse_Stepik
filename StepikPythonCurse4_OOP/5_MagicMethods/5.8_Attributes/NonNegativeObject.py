class NonNegativeObject:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, str) or value >= 0:
                setattr(self, key, value)
            else:
                setattr(self, key, -value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)
point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)