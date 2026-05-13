class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, c=1):
        self.value += c

    def dec(self, c=1):
        self.value = max(self.value - c, 0)

class DoubledCounter(Counter):
    def inc(self, c=1):
        self.value += c*2

    def dec(self, c=1):
        self.value = max(self.value - c*2, 0)
