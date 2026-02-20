from functools import singledispatchmethod

class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_iterable(self, iterable):
        self.ipaddress = '.'.join(map(str, iterable))

    def __str__(self):
        return self.ipaddress
    
    def __repr__(self):
        return f"IPAddress('{str(self.ipaddress)}')"

    
ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))