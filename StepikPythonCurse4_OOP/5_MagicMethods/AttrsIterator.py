class AttrsIterator:

    def __init__(self, obj):
        self.attributes = list(obj.__dict__.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.attributes):
            attr = self.attributes[self.index]
            self.index += 1
            return attr
        else:
            raise StopIteration

class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)