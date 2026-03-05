class CountCalls:
    """
    декоратор @CountCalls, который считает количество вызовов декорируемой функции. 
    Счетчик вызовов должен быть доступен по атрибуту calls.
    Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение 
    декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных 
    и именованных аргументов.
    Примечание 2. При сдаче решения декоратор @CountCalls вызывать не нужно.
    """
     
    def __init__(self, func):
        
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def square(a):
    return a ** 2
    
for i in range(100):
    square(i)
    
print(square.calls)