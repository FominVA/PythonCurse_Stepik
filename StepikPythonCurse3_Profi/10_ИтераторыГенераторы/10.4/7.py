class PowerOf:
    def __init__(self, number):
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.number**self.counter
        self.counter += 1
        return result