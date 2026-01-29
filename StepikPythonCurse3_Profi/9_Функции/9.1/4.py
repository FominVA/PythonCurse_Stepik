def non_negative_even(numbers):
    return all(map(lambda x: True if x>= 0 and x%2==0 else False, numbers))



print(non_negative_even([0, 2, 4, 8, 16]))