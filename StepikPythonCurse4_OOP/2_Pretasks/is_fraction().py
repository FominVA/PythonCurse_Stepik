import re
from fractions import Fraction

def is_fraction(string):
    if string == '.' or string == '':
        return False
    pattern = r"^-?\d+/\d*[1-9]\d*$"
    return bool(re.match(pattern, string))

def is_fraction(string):
    try:
        Fraction(string)
        return '/' in string
    except (ZeroDivisionError, ValueError):
        return False