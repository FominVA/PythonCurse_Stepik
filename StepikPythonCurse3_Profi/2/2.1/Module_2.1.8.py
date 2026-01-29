def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))
        


print(print_given(b=2, d=4, c=3, a=1))




# # INPUT DATA:

# # TEST_1:
# print_given(1, [1, 2, 3], 'three', two=2)

# # TEST_2:
# print_given('apple', 'cherry', 'watermelon')

# # TEST_3:
# print_given(b=2, d=4, c=3, a=1)

# # TEST_4:
# print_given()

# # TEST_5:
# print_given(map, range, filter)

# # TEST_6:
# print_given([1, 2, 3, 4], ('a', 'b', 'c', 'd'), name='Timur', age=29, city='Moscow')

# # TEST_7:
# print_given({1: 1, 2: 2, 3: 3}, [1, 2, 3, 4], (0, 0), zxc=123, abc=321, asd=987, iop=765)

# # TEST_8:
# print(print_given())

# # OUTPUT DATA:

# # TEST_1:
# 1 <class 'int'>
# [1, 2, 3] <class 'list'>
# three <class 'str'>
# two 2 <class 'int'>

# # TEST_2:
# apple <class 'str'>
# cherry <class 'str'>
# watermelon <class 'str'>

# # TEST_3:
# a 1 <class 'int'>
# b 2 <class 'int'>
# c 3 <class 'int'>
# d 4 <class 'int'>

# # TEST_4:


# # TEST_5:
# <class 'map'> <class 'type'>
# <class 'range'> <class 'type'>
# <class 'filter'> <class 'type'>

# # TEST_6:
# [1, 2, 3, 4] <class 'list'>
# ('a', 'b', 'c', 'd') <class 'tuple'>
# age 29 <class 'int'>
# city Moscow <class 'str'>
# name Timur <class 'str'>

# # TEST_7:
# {1: 1, 2: 2, 3: 3} <class 'dict'>
# [1, 2, 3, 4] <class 'list'>
# (0, 0) <class 'tuple'>
# abc 321 <class 'int'>
# asd 987 <class 'int'>
# iop 765 <class 'int'>
# zxc 123 <class 'int'>

# # TEST_8:
# None