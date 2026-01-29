import random

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.n:
            num = random.choice(range(self.left, self.right+1))
            self.counter += 1
        else:
            raise StopIteration
        return num


iterator = RandomNumbers(1, 10, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
        