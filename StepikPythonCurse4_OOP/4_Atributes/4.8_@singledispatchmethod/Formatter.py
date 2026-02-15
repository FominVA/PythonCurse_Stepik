from functools import singledispatchmethod

from pygments import formatter


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    @staticmethod
    def _neg_int_float(data: int|float):
        if type(data) is int:
            print(f'Целое число: {data}')
        elif type(data) is float:
            print(f'Вещественное число: {data}')

    @format.register(list)
    @staticmethod
    def _list_method(data):
        print(f"Элементы списка: {str(data)[1:-1]}")

    @format.register(tuple)
    @staticmethod
    def _list_method(data:tuple):
        print(f"Элементы кортежа: {str(data)[1:-1]}")

    @format.register(dict)
    @staticmethod
    def _list_method(data:dict):
        print(f"Пары словаря: {str(data.items())[1:-1]]}")

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))