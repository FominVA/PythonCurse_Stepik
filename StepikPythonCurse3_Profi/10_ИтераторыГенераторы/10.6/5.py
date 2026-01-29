def interleave(*args):
    for i in range(len(args[0])):
        for el in args:
            yield el[i]


print(*interleave('bee', '123'))       