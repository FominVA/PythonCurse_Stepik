import functools

def ignore_exception(*exc):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exception_type = type(e)
                if exception_type in exc:
                    print(f'Исключение {exception_type} обработано')
                    return None
                else:
                    raise
        return wrapper
    return decorator
        
@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x