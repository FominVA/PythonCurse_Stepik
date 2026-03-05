class RomanNumeral:
    _to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    _to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, number):
        self.number = number
        self.int_value = self._roman_to_int(number)


    @classmethod
    def _roman_to_int(cls, s):
        res = 0
        for i in range(len(s)):
            value = cls._to_int_map[s[i]]
            if i + 1 < len(s) and cls._to_int_map[s[i+1]] > value:
                res -= value
            else:
                res += value
        return res

    @classmethod
    def _int_to_roman(cls, n):
        res = []
        for val, symbol in cls._to_roman_map:
            while n >= val:
                res.append(symbol)
                n -= val
        return "".join(res)

    def __str__(self):
        return self.roman_value

    def __int__(self):
        return self.int_value

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_value == other.int_value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_value < other.int_value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_value <= other.int_value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_value > other.int_value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RomanNumeral):
            return self.int_value >= other.int_value
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            new_int = self.int_value + other.int_value
            return RomanNumeral(self._int_to_roman(new_int))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            new_int = self.int_value - other.int_value
            return RomanNumeral(self._int_to_roman(new_int))
        return NotImplemented