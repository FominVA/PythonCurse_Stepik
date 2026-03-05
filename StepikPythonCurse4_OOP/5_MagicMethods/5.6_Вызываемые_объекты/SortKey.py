class SortKey:

    def __init__(self, *args):
        self.args = args

    def __call__(self, user):
        if len(self.args) == 1:
            return getattr(user, self.args[0])
        return tuple(getattr(user, attr) for attr in self.args)
    
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))