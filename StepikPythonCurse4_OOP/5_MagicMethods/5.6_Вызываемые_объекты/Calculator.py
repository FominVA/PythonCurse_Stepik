class Calculator:

    def __init__(self):
        pass

    def __call__(self, a, b, operation):
        if operation == '+':
            return a+b
        elif operation == '-':
            return a-b
        elif operation == '*':
            return a*b
        elif operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        else:
            return a/b

        
calculator = Calculator()

print(calculator(10, 0, '+'))
print(calculator(10, 0, '-'))
print(calculator(10, 0, '*'))