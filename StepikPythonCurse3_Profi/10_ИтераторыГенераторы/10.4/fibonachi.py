class Fibonacci:
    def __init__(self):
        self.current = 1
        self.next = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.current
        self.current = self.next
        self.next = result+self.next
        return result


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))