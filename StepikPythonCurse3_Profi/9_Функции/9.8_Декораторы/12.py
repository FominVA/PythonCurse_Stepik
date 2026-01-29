import functools

class MaxRetriesException(Exception):
    pass

def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for time in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if time == times - 1:
                        raise MaxRetriesException
        return wrapper
    return decorator
        
@retry(3)
def no_way():
    raise ValueError
   
try:
    no_way()
except Exception as e:
    print(type(e))
