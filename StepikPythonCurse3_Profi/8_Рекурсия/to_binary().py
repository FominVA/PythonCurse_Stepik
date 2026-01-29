def to_binary(number):   
    if number < 2:
        return str(number)
    else:
        return to_binary(number//2) + str(number%2)