def convert(string):
    Up = []
    Low = []
    for i in string:
        if i.isupper():
            Up.append(i)
        if i.islower():
            Low.append(i)
    if len(Up) > len(Low):
        return string.upper()
    else:
        return string.lower()
    



print(convert('dEfAbC'))



# # INPUT DATA:

# # TEST_1:
# print(convert('BEEgeek'))

# # TEST_2:
# print(convert('pyTHON'))

# # TEST_3:
# print(convert('pi31415!'))

# # TEST_4:
# print(convert('ABCDEF'))

# # TEST_5:
# print(convert('abcdef'))

# # TEST_6:
# print(convert('12345!?'))

# # TEST_7:
# print(convert('PI31415!'))

# # TEST_8:
# print(convert('ABCdef'))

# # TEST_9:
# print(convert('ABCdef123'))

# # TEST_10:
# print(convert('AbCdEf12345'))

# # TEST_11:
# print(convert('dEfAbC'))


# # OUTPUT DATA:

# # TEST_1:
# beegeek

# # TEST_2:
# PYTHON

# # TEST_3:
# pi31415!

# # TEST_4:
# ABCDEF

# # TEST_5:
# abcdef

# # TEST_6:
# 12345!?

# # TEST_7:
# PI31415!

# # TEST_8:
# abcdef

# # TEST_9:
# abcdef123

# # TEST_10:
# abcdef12345

# # TEST_11:
# defabc