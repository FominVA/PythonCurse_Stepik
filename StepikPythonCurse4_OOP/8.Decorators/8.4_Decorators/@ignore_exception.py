import functools

class ignore_exception:

    def __init__(self, *excps):
        self.excps = excps

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for excp in self.excps:
                    if isinstance(e, excp):
                        print(f'Исключение {type(e).__name__} обработано')
                        return
                raise e
        return wrapper



min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))