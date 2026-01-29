def is_greater(lists, number):
    return any(map(lambda x: True if sum(x)>number else False, lists))

data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

print(is_greater(data, 2))