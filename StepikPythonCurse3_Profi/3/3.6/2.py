import time

def get_the_fastest_func(funcs, arg):
    l = []
    for func in funcs:
        start = time.perf_counter()
        result = func(arg)
        end = time.perf_counter()
        t = end - start
        l.append(t)
    minimum = min(l)
    return funcs[l.index(minimum)]
