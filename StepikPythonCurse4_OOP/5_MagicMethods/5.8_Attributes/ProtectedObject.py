class ProtectedObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)

    def __getattribute__(self, item):
        # Если имя начинается с '_', запрещаем доступ
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        # Если имя начинается с '_', запрещаем создание или изменение
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        # Если имя начинается с '_', запрещаем удаление
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        super().__delattr__(item)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)