class SuperString:

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
    
    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string+other.string)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int):
            return SuperString(self.string*n)
        return NotImplemented
    
    def __rmul__(self, n):
        if isinstance(n, int):
            return SuperString(n*self.string)
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, int):
            m = int(len(self.string)/n)
            return SuperString(self.string[:m])
        return NotImplemented
        
    def __lshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.string):
                return SuperString('')
            else:
                return SuperString(self.string[:(len(self.string)-n)])
        return NotImplemented
    
    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.string):
                return SuperString('')
            else:
                return SuperString(self.string[n:])
        return NotImplemented
    
s1 = SuperString('bee')
s2 = SuperString('geek')

new_s1 = s1 << 1
new_s2 = s2 >> 1
new_s3 = s1 + s2
new_s4 = s1 * 2
new_s5 = s2 / 2

print(new_s1, type(new_s1))
print(new_s2, type(new_s2))
print(new_s3, type(new_s3))
print(new_s4, type(new_s4))
print(new_s5, type(new_s5))