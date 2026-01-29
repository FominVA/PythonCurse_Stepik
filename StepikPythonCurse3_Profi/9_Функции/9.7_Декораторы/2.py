def decorator(func):
    def wrapper(*args, **kwargs):
        new_args = (i.upper() if isinstance(i, str) and i.isalpha() else i for i in args)
        new_kwargs = {key: value.upper() for key, value in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

print=decorator(print)

print('hi', 'there', end='!')