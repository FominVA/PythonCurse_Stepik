from dataclasses import dataclass

@dataclass
class ArithmeticProgression:
    el: int
    step: int

    def __iter__(self):
        current = self.el
        while True:
            yield current
            current += self.step

@dataclass
class GeometricProgression:
    el: int
    step: int

    def __iter__(self):
        current = self.el
        while True:
            yield current
            current *= self.step


progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8


