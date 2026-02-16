class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    @property
    def fullname(self):
        return self.name + " " + self.surname

    @fullname.setter
    def fullname(self, name):
        if isinstance(name, str) and name != "":
            self.name, self.surname = name.split()
        else:
            raise ValueError("Name must be a string")

person = Person('Mike', 'Pondsmith')

print(person.name)
print(person.surname)
print(person.fullname)