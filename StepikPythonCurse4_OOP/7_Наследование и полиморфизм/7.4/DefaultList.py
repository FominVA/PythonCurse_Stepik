from collections import UserList

class DefaultList(UserList):

    def __init__(self, iterable=[], default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, item):
        try:
            return self.data[item]
        except:
            return self.default

defaultlist = DefaultList([1, 2, 3], 0)

print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])