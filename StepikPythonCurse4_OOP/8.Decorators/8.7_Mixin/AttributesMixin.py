
class AttributesMixin:

    def get_public_attributes(self):
        l = []
        for key in self.__dict__:
            if key[0] != '_':
                l.append((key, self.__getattribute__(key)))
        return l

    def get_protected_attributes(self):
        l = []
        for key in self.__dict__:
            if key[0] == '_' and '__' not in key:
                l.append((key, self.__getattribute__(key)))
        return l


class Cat(AttributesMixin):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self._breed = breed


cat = Cat('Кемаль', 6, 'Британский')
print(cat.get_public_attributes())
print(cat.get_protected_attributes())