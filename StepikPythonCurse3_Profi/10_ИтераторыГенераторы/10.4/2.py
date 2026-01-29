class StringWrapper:                             
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.index = -1                     # вспомогательное поле для отслеживания текущего индекса
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.text):
            raise StopIteration
        return self.symbol + self.text[self.index] + self.symbol


string_wrapper1 = StringWrapper('beegeek', '~')

print(list(string_wrapper1))