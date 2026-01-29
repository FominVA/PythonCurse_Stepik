import sys 
class PasswordError(Exception):
    pass

class LengthError(Exception):
    pass

class LetterError(Exception):
    pass

class DigitError(Exception):
    pass

def is_good_password(string):
    try:
        letters = [char for char in string if char.isalpha()]

        if len(string) >= 9 and any(char.isupper() for char in letters) and any(char.islower() for char in letters) and any(i.isdigit() for i in string):
            return True
        if len(string) < 9:
            raise LengthError()
    
        if not letters:
            raise LetterError("Password must contain letters.")
        
        has_upper = any(char.isupper() for char in letters)
        has_lower = any(char.islower() for char in letters)
    
        if not (has_upper and has_lower):
            raise LetterError("Password must contain both uppercase and lowercase letters.")
            
        if not any(i.isdigit() for i in string):
            raise DigitError()
    except (LengthError, LetterError, DigitError) as e:
        return type(e)

string = [line.strip() for line in sys.stdin]
for i in string:
    is_good_password(i)
print('Success!')