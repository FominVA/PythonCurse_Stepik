class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, c=1):
        self.value += c

    def dec(self, c=1):
        self.value = max(self.value - c, 0)

class NonDecCounter(Counter):
    def dec(self, c=1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.value = start
        self.limit = limit

    def inc(self, c=1):
        self.value = min(self.value + c, self.limit)

counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)