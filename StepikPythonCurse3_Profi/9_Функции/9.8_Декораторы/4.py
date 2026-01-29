import functools
def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = string+func(*args, **kwargs)
            if to_the_end:
                result = func(*args, **kwargs)+string
            return result
        return wrapper
    return decorator


@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())
