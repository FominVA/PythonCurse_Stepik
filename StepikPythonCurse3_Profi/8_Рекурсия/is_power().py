def is_power(number):
    if number <= 2:
        return True
    elif number%2 == 1:
        return False
    return is_power(number/2) 
print(is_power(1))