def get_method_owner(cls, method):
    for cl in cls.mro():
        if method in cl.__dict__:
            return cl


class A:
    def m(self):
        pass


class B(A):
    pass


print(get_method_owner(B, 'm'))