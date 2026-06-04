class EasyDict(dict):

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(self, item)
        except:
            return self[item]




easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(easydict.city)