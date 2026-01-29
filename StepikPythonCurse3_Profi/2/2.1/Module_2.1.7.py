def is_valid(string):
    if string == '':
        return False
    else:
        return all(list(map(lambda x: True if len(string) > 3 and len(string) < 7 and string.isdigit() and len(string) != 0 else False, string)))




print(is_valid(''))





# # TESTS - просто размести их под кодом
# #assert is_valid('4367') == True
# #assert is_valid('92134') == True
# #assert is_valid('89abc1') == False
# #assert is_valid('900876') == True
# assert is_valid('49 83') == False
# assert is_valid('467') == False
# assert is_valid('4323423424467') == False
# assert is_valid('3 7 0') == False
# assert is_valid('0000') == True
# assert is_valid('') == False
# assert is_valid('aaaa') == False
# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК )
