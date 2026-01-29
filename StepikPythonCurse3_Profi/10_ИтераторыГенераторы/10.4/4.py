class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.obj
        return result

bee = Repeater('bee')

print(next(bee))