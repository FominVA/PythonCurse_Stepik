def is_good_password(string):
    if len(string) >= 9 and string != string.upper() and string != string.lower() and any(i.isdigit() for i in string):
        return True
    else:
        return False