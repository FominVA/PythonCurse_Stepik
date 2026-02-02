import re


def is_integer(num):
    pattern = '^\-?\d+$'
    result = re.findall(pattern, num)
    return bool(len(result))

print(is_integer('199.1'))