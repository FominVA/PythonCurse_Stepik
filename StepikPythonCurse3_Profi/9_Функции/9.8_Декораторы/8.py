import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, datatype):
                raise TypeError
            return result
        return wrapper
    return decorator


@returns(int)
def add(a, b):
    return a + b

try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))