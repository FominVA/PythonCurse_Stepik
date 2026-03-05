class Temperature:

    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        result = (self.temperature*9/5)+32
        return result
    
    @classmethod
    def from_fahrenheit(cls, F):
        C = (5/9)*(F-32)
        return Temperature(C)
        
    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)
        
    def __str__(self):
        return f'{round(self.temperature, 2)}°C'
    
    def __bool__(self):
        return self.temperature > 0
    
t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)

print(bool(t1))
print(bool(t2))
print(bool(t3))