def get_biggest(numbers):
    if len(numbers) == 0:
        return 1
    else:
        s =''
        new_numbers = sorted(numbers, reverse=True)
        for i in new_numbers:
            s += str(i)
        return s

print(get_biggest([7, 71, 72]))




# # TESTS - просто размести их под кодом (нет 9 и 15 теста)

# assert get_biggest([1, 2, 3])  == 321
# assert get_biggest([61, 228, 9, 3, 11]) == 961322811
# assert get_biggest([7, 71, 72]) == 77271
# assert get_biggest([]) == -1
# assert get_biggest([0, 0, 0, 0, 0, 0]) == 0
# assert get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]) == 78554656558534233433222211311
# assert get_biggest([7, 7, 7, 7, 7, 7, 7, 7, 7]) == 777777777
# assert get_biggest([62, 626]) == 62662
# assert get_biggest([9, 6, 3, 0, 3, 6, 9]) == 9966330
# assert get_biggest([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 9876543210
# assert get_biggest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 987654321100
# assert get_biggest([1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 98765432110
# assert get_biggest([3]) == 3

# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК )