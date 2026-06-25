import json

class JsonSerializableMixin:

    def to_json(self):
        return json.dumps(self.__dict__)

class Triangle(JsonSerializableMixin):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

triangle = Triangle(3, 5, 4)
print(triangle.to_json())