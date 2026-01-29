
def square(func) -> int | float:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)**2
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@square
def add(a, b):
    return a + b

print(add(3, 7))
