class User:
    def __init__(self, name, age):
        if str(name).isalpha() and isinstance(name, str):
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        if str(age).isdigit() and 110 >= age >= 0:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if str(new_name).isalpha() and isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')
            
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if str(new_age).isdigit() and 110 >= new_age >= 0:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')


user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)