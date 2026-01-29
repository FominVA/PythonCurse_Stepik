def print_digits(number):
    if number < 10:
        print(number)
    else:
        print(number%10)
        print_digits(number//10)


print_digits(4868569493888292933)