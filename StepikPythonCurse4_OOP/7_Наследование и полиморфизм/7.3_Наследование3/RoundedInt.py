
class RoundedInt(int):
    def __new__(cls, num, even=True):
        value = int(num)
        if (value % 2 == 0) != even:
            value += 1
        instance = super().__new__(cls, value)
        instance.even = even
        return instance

roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
