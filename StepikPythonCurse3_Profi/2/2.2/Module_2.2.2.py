def language(a, b, c):
    not_ascii = []
    for i in letters:
        if ord(i) > 1000:
            not_ascii.append(ord(i))
    if len(not_ascii) == 3:
        return 'ru'
    elif len(not_ascii) == 0:
        return 'en'
    else:
        return 'mix'


a, b, c = input(), input(), input()
letters = [a, b, c]
print(language(a, b, c))



# # INPUT DATA:

# # TEST_1:
# Р
# О
# А

# # TEST_2:
# o
# K
# M

# # TEST_3:
# T
# а
# B

# # TEST_4:
# а
# К
# о

# # TEST_5:
# E
# c
# T

# # TEST_6:
# H
# Н
# B

# # TEST_7:
# H
# p
# T

# # TEST_8:
# Н
# р
# Т

# # TEST_9:
# р
# р
# p

# # TEST_10:
# а
# а
# а

# # TEST_11:
# x
# x
# x

# # OUTPUT DATA:

# # TEST_1:
# ru

# # TEST_2:
# en

# # TEST_3:
# mix

# # TEST_4:
# ru

# # TEST_5:
# en

# # TEST_6:
# mix

# # TEST_7:
# en

# # TEST_8:
# ru

# # TEST_9:
# mix

# # TEST_10:
# ru

# # TEST_11:
# en