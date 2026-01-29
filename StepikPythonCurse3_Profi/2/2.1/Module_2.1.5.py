def hide_card(card_number):
    card_number = card_number.replace(' ', '')
    if len(card_number) == 16:
        new_cardnum = '*'*12 + card_number[12:]
    return new_cardnum
    
card = '7 3 9 1 4 0 5 6 5 2 7 8 9 4 3 4'

print(hide_card(card))


# INPUT DATA:

# TEST_1:
#card = '1234567890123456'

#print(hide_card(card))

# TEST_2:
#card = '3456 9012 5678 1234'

#print(hide_card(card))

# TEST_3:
#card = '905 678123 45612 56'

#print(hide_card(card))

# TEST_4:
#card = '7 3 9 1 4 0 5 6 5 2 7 8 9 4 3 4'
#print(hide_card(card))

# TEST_5:
#card = '  103 43948 19446 323  '
#print(hide_card(card))

# TEST_6:
#print(hide_card('1034 3948 1944 6327'))


# OUTPUT DATA:

# TEST_1:
#************3456

# TEST_2:
#************1234

# TEST_3:
#************1256

# TEST_4:
#************9434

# TEST_5:
#************6323

# TEST_6:
#************6327