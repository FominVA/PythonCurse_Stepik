import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            s_list = list(func(*args, **kwargs))
            for i in range(start, end):
                if 0 <= i < len(s_list):
                    s_list[i] = char
            return "".join(s_list)
        return wrapper
    return decorator

@strip_range(3, 5)
def beegeek():
    return 'beegeek'
    
print(beegeek())