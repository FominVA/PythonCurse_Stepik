def my_pow(number):
    number = enumerate(list(str(number)), 1)
    result = [int(v)**k for k, v in number]
    return sum(result)

print(my_pow(139))