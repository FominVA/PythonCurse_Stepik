def same_parity(numbers):
    l = []
    if len(numbers) == 0:
        return l
    else:
        return list(filter(lambda num: numbers[0] % 2 == num % 2, numbers))
    

numbers = [1, 3, 5, 7, 9]
print(same_parity(numbers))


#assert same_parity([]) == []
#assert same_parity([6, 0, 67, -7, 10, -20]) == [6, 0, 10, -20]
#assert same_parity([-7, 0, 67, -9, 70, -29, 90]) == [-7, 67, -9, -29]
#assert same_parity([2]) == [2]
#assert same_parity([2, 2, 2, 2, 3, 0, 2, 3]) == [2, 2, 2, 2, 0, 2]
#assert same_parity([-1, 1248234832443, 8]) == [-1, 1248234832443]
#assert same_parity([1, 2, 4, 6, 8]) == [1]
#assert same_parity([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
#print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК )