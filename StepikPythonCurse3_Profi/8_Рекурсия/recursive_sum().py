def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a+1, b-1)
print(recursive_sum(10, 22))