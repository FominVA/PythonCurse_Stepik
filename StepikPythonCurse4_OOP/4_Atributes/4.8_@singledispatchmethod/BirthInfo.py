from functools import singledispatchmethod
from datetime import date

class BirthInfo:
    
    @singledispatchmethod
    def _process_date(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @_process_date.register(date)
    def _from_date(self, birth_date):
        return birth_date

    @_process_date.register(str)
    def _from_str(self, birth_date):
        try:
            return date.fromisoformat(birth_date)
        except ValueError:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @_process_date.register(list)
    @_process_date.register(tuple)
    def _from_collection(self, birth_date):
        try:
            return date(*birth_date)
        except (ValueError, TypeError):
            raise TypeError('Аргумент переданного типа не поддерживается')

    def __init__(self, birth_date):
        self.birth_date = self._process_date(birth_date)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    
birthday = date(2020, 9, 18)
today = date.today()
birthinfo = BirthInfo(birthday)

    