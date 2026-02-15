from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register
    @staticmethod
    def _neg_int_float(data: int|float):
        return -data

    @neg.register
    @staticmethod
    def _bool_method(data):
        if data:
            return False
        else:
            return True
