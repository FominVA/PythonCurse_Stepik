from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self.name]
        except:
            raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    @abstractmethod
    def validate(self):
        pass

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if not isinstance(obj, int|float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        elif self.minvalue is not None and obj < self.minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        elif self.maxvalue is not None and obj > self.maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        elif self.minsize is not None and len(obj) < self.minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        elif self.maxsize is not None and len(obj) > self.maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        elif self.predicate:
            raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")

class Person:
    name = String(6, 10, predicate=lambda x: x.startswith('А'))


person = Person()

try:
    person.name = 'Василий'
except ValueError as e:
    print(e)

