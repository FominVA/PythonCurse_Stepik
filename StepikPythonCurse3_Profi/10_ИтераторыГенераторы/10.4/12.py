class Alphabet:
    def __init__(self, language):
        self.alp = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.language = language
        self.counter = 0
        self.length = len(self.alp[self.language])
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter <= self.length:
            result = self.alp[self.language][self.counter]
            self.counter += 1
        else:
            raise StopIteration
        return result

ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))