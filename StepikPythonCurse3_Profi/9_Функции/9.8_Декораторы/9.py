import functools

def takes(*arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for types in (*args,*kwargs.values()):
                if type(types) not in arg:
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))