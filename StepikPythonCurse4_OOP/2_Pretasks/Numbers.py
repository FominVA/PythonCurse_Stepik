class Numbers:
    def __init__(self):
        self.even = []
        self.odd = []
    
    def add_number(self, num): #метод, принимающий в качестве аргумента целое число и добавляющий его в набор
        if num % 2 == 0:
            self.even.append(num)
        else:
            self.odd.append(num)

    def get_even(self): #метод, возвращающий список всех четных чисел из набора
        return self.even
    
    def get_odd(self): #метод, возвращающий список всех нечетных чисел из набора
        return self.odd