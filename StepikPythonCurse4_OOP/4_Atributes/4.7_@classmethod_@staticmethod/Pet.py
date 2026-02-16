class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        if not cls.pets:
            return None
        return cls.pets[0]

    @classmethod
    def last_pet(cls):
        if not cls.pets:
            return None
        return cls.pets[-1]

    @classmethod
    def number_of_pets(cls):
        if not cls.pets:
            return 0
        return len(cls.pets)
