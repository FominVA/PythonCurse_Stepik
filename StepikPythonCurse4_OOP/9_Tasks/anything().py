import math, re

def anything():
    class Anything:
        def __ne__(self, other):
            return True

        def __lt__(self, other):
            return True

        def __le__(self, other):
            return True

        def __gt__(self, other):
            return True

        def __ge__(self, other):
            return True

        def __eq__(self, other):
            return True

        def __call__(self, *args, **kwargs):
            return self
    return Anything()

print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)