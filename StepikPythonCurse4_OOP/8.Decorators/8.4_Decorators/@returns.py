import functools

class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, self.datatype):
                return result
            else:
                raise TypeError
        return wrapper


@returns(int)
def add(a, b):
    return a + b

print(add(1, 2))