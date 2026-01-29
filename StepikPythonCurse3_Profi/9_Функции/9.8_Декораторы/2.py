def returns_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise TypeError
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@returns_string
def beegeek():
    return 'beegeek'
    
print(beegeek())