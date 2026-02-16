from functools import singledispatchmethod

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(float)
    @process.register(int)
    @staticmethod
    def _int_float_method(data: int|float):
        return data * 2

    @process.register(str)
    @staticmethod
    def _str_method(data: str):
            return data.upper()

    @process.register(list)
    @staticmethod
    def _list_method(data:list):
            return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _tuple_method(data:tuple):
            return tuple(sorted(data))

print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))