class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'

class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass

son = Son()

print(son.greet())
print(son.mood)
son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)