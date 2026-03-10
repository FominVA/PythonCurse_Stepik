class DefaultObject:

    def __init__(self, default=None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, name):
        return self.default

god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)