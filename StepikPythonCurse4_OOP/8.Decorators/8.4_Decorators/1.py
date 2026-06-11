a = [int, int]
b = (1, '2')


for el in list(zip(a, b)):
    if isinstance(el[1], el[0]) is True:
        print('Yes')