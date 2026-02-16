from math import sqrt
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        return (-self.b-(sqrt(self.b**2-4*self.a*self.c)))/(2*self.a)
    
    @property
    def x2(self):
        return (-self.b+(sqrt(self.b**2-4*self.a*self.c)))/(2*self.a)
    
    @property
    def view(self):
        a = self.a
        if 
        

        return f'{a}x^2 + bx + c'
            

    
    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    
    @coefficients.setter
    def coefficients(self, coefficient):
        if isinstance(coefficient, tuple) and len(coefficient) == 3:
            self.a, self.b, self.c = coefficient
        