import functools

class takes_numbers:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if not isinstance(arg, int|float):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)

@takes_numbers
def mul(a, b):
    return a * b

print(mul(a=1, b=2))