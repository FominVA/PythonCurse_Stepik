def power(degree):
    def func(x):
        return x**degree
    return func
    

square = power(2)
print(square(5))