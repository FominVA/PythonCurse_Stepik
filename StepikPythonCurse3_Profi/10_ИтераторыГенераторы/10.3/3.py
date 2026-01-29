from random import choice

def random_numbers(left, right):
    l = list(range(left, right+1))
    return choice(l)

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))