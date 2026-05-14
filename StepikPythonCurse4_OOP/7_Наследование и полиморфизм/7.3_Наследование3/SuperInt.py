class SuperInt(int):
    def __new__(cls, n, *args, **kwargs):
        s = super().__new__(cls, str(n))
        return s

    def repeat(self, n=2):
        if self < 0:
            return SuperInt('-' + str(-self) * n)
        else:
            return SuperInt(str(self) * n)

    def to_bin(self):
        """Возвращает двоичное представление числа в виде строки.
        Для отрицательных чисел добавляется минус."""
        if self >= 0:
            return bin(self)[2:]
        else:
            return '-' + bin(abs(self))[2:]

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        """Итерация по цифрам числа (для отрицательных – по цифрам модуля)."""
        digits = str(abs(self))
        return (SuperInt(int(d)) for d in digits)

superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())