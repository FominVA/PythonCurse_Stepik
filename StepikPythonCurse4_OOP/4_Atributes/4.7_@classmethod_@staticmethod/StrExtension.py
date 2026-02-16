class StrExtension:

    @staticmethod
    def remove_vowels(string):
        new_string = ""
        for char in string:
            if char not in "aeiou":
                new_string += char
        return new_string

    @staticmethod
    def leave_alpha(string):
        new_string = ""
        for char in string:
            if char.isalpha():
                new_string += char
        return new_string

    @staticmethod
    def replace_all(string, chars, char):
        for c in string:
            if c in chars:
                string = string.replace(c, char)
        return string