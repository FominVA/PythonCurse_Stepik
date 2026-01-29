def takes_positive(func):
    def wrapper(*args,**kwargs):
        all_values = args + tuple(kwargs.values())
        for value in all_values:
            if not isinstance(value, int):
                raise TypeError
        for value in all_values:
            if value <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper



@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-1, 2, 3, 4.2))
except Exception as err:
    print(type(err))