class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.data = []
        for i in iterable:
            self.data.append(i)
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.data):
            result = self.data[self.counter]
            self.counter += 1
        else:
            raise StopIteration
        

cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))
        