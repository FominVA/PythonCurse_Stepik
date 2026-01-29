def reverse(sequence):
    result = reversed(sequence)
    for i in result:
        yield i


print(*reverse([1, 2, 3, 4, 5]))