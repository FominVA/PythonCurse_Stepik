def index_of_nearest(numbers, number):
    new_numbers = []
    if len(numbers) == 0:
        return -1
    else:
        for num in numbers:
            new_numbers.append(abs(num-number))
        x = new_numbers.index(min(new_numbers))
        return x


print(index_of_nearest([9, 5, 3, 2, 11], 4))

# print(index_of_nearest([], 17)) #-1
# print(index_of_nearest([7, 13, 3, 5, 18], 0)) #2
# print(index_of_nearest([9, 5, 3, 2, 11], 4)) #1
# print(index_of_nearest([7, 5, 4, 4, 3], 4)) #2
# print(index_of_nearest([6, 100, 101, 2], 4)) #0
# print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)) #3
# print(index_of_nearest([1, 14, 100, 65, 6], 5)) #4
# print(index_of_nearest([10, 164, 100, 265, 16], 8)) #0
# print(index_of_nearest([10, 99, 0, -12, 16], -9)) #3
# print(index_of_nearest([1, 1, 1, 1, 1], 1)) #0