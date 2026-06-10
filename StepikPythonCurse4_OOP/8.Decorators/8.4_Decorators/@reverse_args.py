import functools

class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)

@reverse_args
def operation(a, b, value1=10, value2=30):
    return a // b - value1 + value2

print(operation(140, 70, value1=50, value2=100))
