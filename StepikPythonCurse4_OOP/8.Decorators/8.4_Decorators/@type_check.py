import functools

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, self.types):
                if not isinstance(arg, expected_type):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper


@type_check([int, int, str])
def add(a, b, c=3):
    return a + b + c


print(add(1, 2, c=5))