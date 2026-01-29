class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.end - self.start) <= abs(self.step):
            raise StopIteration
        self.start += self.step
        return self.start
evens = Xrange(0, 10, 2)

print(*evens)
