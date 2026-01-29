def cyclic_shift(numbers: list[int | float], step: int) -> None:
    numbers[:] = [numbers[(i - step) % len(numbers)] for i in range(len(numbers))]
    return numbers

numbers = [1, 2, 3, 4, 5]
print(cyclic_shift(numbers, 1))