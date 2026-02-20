class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = str(phone_number).replace(' ', '')

    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:10]}'
        
    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"
    
phone = PhoneNumber('9173963385')

print(str(phone))
print(repr(phone))