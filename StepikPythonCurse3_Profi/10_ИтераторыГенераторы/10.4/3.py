class Factorials:
    def __init__(self):
        self.value = 1
        self.index = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value
    
for index, value in enumerate(Factorials(), 1):
    if index <= 10:
        print(f'Факториал числа {index} равен {value}')
    else:
        break