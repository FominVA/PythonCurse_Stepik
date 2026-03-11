class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__['attrs_num'] = 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__['attrs_num'] += 1
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            del self.__dict__[item]
            self.__dict__['attrs_num'] -= 1

    @property
    def attrs_num(self):
        # Возвращаем текущее значение счетчика
        return self.__dict__['attrs_num']


music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)