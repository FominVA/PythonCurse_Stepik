Roman_numerals = {10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
Arabic_numerals = {'X':10, "IX":9, "V":5, 'IV':4, 'I':1}


def to_arabic(number):
    result = 0
    for numeral, num in Arabic_numerals.items():
        while number:
            if numeral in number:
                result += num
                number = number[len(numeral):]
    return result 

print(to_arabic('XV'))