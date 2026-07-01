class Predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        if isinstance(other, Predicate):
            return Predicate(lambda *a, **kw: self(*a, **kw) and other(*a, **kw))
        raise TypeError("& поддерживается только между экземплярами Predicate")

    def __or__(self, other):
        if isinstance(other, Predicate):
            return Predicate(lambda *a, **kw: self(*a, **kw) or other(*a, **kw))
        raise TypeError("| поддерживается только между экземплярами Predicate")

    def __invert__(self):
        return Predicate(lambda *a, **kw: not self(*a, *kw))

def predicate(func):
    return Predicate(func)


@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
print((~is_even & is_positive)(3))            # True; равнозначно not is_even(3) and is_positive(3)