import time

def calculate_it(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    t = end - start
    return (result, t)
