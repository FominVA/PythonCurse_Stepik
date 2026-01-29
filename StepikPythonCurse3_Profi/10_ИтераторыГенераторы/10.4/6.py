class Square:
    def __init__(self, n):
        self.n = n
        self.counter = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter <= self.n:
            result = self.counter**2
            self.counter += 1
            return result
        else:
            raise StopIteration


squares = Square(10)

print(list(squares))