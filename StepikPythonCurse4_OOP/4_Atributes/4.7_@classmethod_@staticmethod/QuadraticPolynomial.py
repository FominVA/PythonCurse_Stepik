class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        a, b, c = iterable
        return cls(a, b, c)

    @classmethod
    def from_str(cls, string):
        a, b, c = string.split()
        return cls(float(a), float(b), float(c))

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)