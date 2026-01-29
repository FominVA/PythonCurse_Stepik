def choose_plural(amount, declensions):
    s = [str(num) for num in range(11, 20)]
    l = ['2', '3', '4']
    if str(amount)[-1] == '1' and str(amount)[(len(str(amount))-2):(len(str(amount)))] not in s:
        return f'{str(amount)} {declensions[0]}'
    elif str(amount)[-1] in l and str(amount)[(len(str(amount))-2):(len(str(amount)))] not in ['12', '13', '14']:
        return f'{str(amount)} {declensions[1]}'
    else:
        return f'{str(amount)} {declensions[2]}'


print(choose_plural(1, ('пример', 'примера', 'примеров')))



# # INPUT DATA:

# # TEST_1:
# print(choose_plural(21, ('пример', 'примера', 'примеров')))

# # TEST_2:
# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

# # TEST_3:
# print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))

# # TEST_4:
# print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))

# # TEST_5:
# print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))

# # TEST_6:
# print(choose_plural(512312, ('цент', 'цента', 'центов')))

# # TEST_7:
# print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))

# # TEST_8:
# print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))

# # TEST_9:
# print(choose_plural(240, ('курица', 'курицы', 'куриц')))

# # TEST_10:
# print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))

# # TEST_11:
# print(choose_plural(505, ('утка', 'утки', 'уток')))

# # TEST_12:
# print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))

# # TEST_13:
# print(choose_plural(11, ('стул', 'стула', 'стульев')))

# # TEST_14:
# print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))

# # TEST_15:
# print(choose_plural(2, ('пример', 'примера', 'примеров')))

# # TEST_16:
# print(choose_plural(111, ('пример', 'примера', 'примеров')))

# # TEST_17:
# print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))




# # OUTPUT DATA:

# # TEST_1:
# 21 пример

# # TEST_2:
# 92 гвоздя

# # TEST_3:
# 8 яблок

# # TEST_4:
# 111223 копейки

# # TEST_5:
# 763434 рубля

# # TEST_6:
# 512312 центов

# # TEST_7:
# 59 помидоров

# # TEST_8:
# 23424157 огурцов

# # TEST_9:
# 240 куриц

# # TEST_10:
# 49324 плюмбуса

# # TEST_11:
# 505 уток

# # TEST_12:
# 666 шкафов

# # TEST_13:
# 11 стульев

# # TEST_14:
# 3458438435812 долларов

# # TEST_15:
# 2 примера

# # TEST_16:
# 111 примеров

# # TEST_17:
# 1223123111 примеров