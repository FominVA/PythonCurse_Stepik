class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
        

    def get_balance(self): #— метод, возвращающий актуальный баланс счета
        return self._balance
    
    def deposit(self, amount): #— метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
        self._balance += amount
        return self._balance 
    
    def withdraw(self, amount): #— метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount. Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
        if self._balance > amount:
            self._balance -= amount
            return self._balance
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account, amount):
        if self._balance > amount:
            self._balance -= amount
            account._balance += amount
            return self._balance
        else:
            raise ValueError('На счете недостаточно средств')
        
account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())   