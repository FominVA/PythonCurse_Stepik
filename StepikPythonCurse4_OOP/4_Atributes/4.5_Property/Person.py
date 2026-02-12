class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        if isinstance(self.name, str) and isinstance(self.surname, str):
            self.full_name = str(self.name) + ' ' + str(self.surname)
        return self.full_name
    
    def set_fullname(self, fullname):
        if isinstance(fullname, str):
            self.name, self.surname = fullname.split()
    
    fullname = property(get_fullname, set_fullname)

person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)