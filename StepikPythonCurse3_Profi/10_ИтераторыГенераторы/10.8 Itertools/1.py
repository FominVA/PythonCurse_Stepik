from itertools import count
def tabulate(func):
    count1 = count(1, 1)
    g = (func(num) for num in count1)
    yield from g

func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))