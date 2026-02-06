import re

def is_decimal(string):
    if string == '.' or string == '':
        return False
    pattern = r'^-?(\d+)?\.?(\d+)?$'
    result = re.fullmatch(pattern, string)
    if result is None:
        return False
    else:
        return True

