class MinStat:
    def __init__(self, iterable=[]):
        self.iterable = iterable

    def add(self, num):
        if isinstance(self.iterable, list):
            self.iterable.append(num)

    def result(self):
        if self.iterable:
            return min(self.iterable)
        else:
            return None

    def clear(self):
        self.iterable = []

class MaxStat(MinStat):

    def result(self):
        if self.iterable:
            return max(self.iterable)
        else:
            return None

class AverageStat(MinStat):

    def result(self):
        if self.iterable:
            return sum(self.iterable)/len(self.iterable)
        else:
            return None

minstat = MinStat([1, 2, 4])


minstat.add(5)

print(minstat.result())