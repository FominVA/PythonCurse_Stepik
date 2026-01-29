def convert(number):
    number1 = bin(number).replace('0b', '')
    number2 = oct(number).replace('0o', '')
    number3 = hex(number).replace('0x', '').upper()
    return (number1, number2, number3)
print(convert(15))