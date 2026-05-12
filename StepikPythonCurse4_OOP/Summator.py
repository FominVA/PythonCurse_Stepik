class Summator:
    degree = 1
    def total(self, n):
        return sum(map(lambda x: x**self.degree, range(1, n+1)))

class SquareSummator(Summator):
    degree = 2

class QubeSummator(Summator):
    degree = 3

class CustomSummator(Summator):
    def __init__(self, m):
        self.degree = m
