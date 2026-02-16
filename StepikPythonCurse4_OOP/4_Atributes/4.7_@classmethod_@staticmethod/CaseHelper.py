import re

class CaseHelper:

    @staticmethod
    def is_snake(string):
        result = re.fullmatch(r"[a-z]+_", string)
        if result:
            return True
        else:
            return False

    @staticmethod
    def is_upper_camel(string):
        result = re.match(r"^[A-Z][a-z]+$|^[A-Z][a-z]+[A-Z][a-z]+$", string)
        if result:
            return True
        else:
            return False

    @staticmethod
    def to_snake(string):
        p = re.findall(r"[A-Z][a-z]+", string)
        if len(p) == 1:
            return p[0].lower()
        else:
            return '_'.join([char.lower() for char in p])

    @staticmethod
    def to_upper_camel(string):
        p = re.findall(r"[a-z]+", string)
        if len(p) == 1:
            return p[0].title()
        else:
            return ''.join(p)

