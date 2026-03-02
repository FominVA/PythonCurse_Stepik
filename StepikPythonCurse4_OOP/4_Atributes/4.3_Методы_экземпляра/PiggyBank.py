import numbers


class PiggyBank:
    def __init__(self, balance=0, volume=400):
        self.balance = balance
        self.volume = volume

    def add_coins(self, coins):
        if self.balance + coins > self.volume:
            print("Копилка слишком мала")
        else:
            self.balance += coins

    def remove_coins(self, coins):
        if self.balance - coins < 0:
            print("В копилке недостаточно денег")
        else:
            self.balance -= coins

piggy = PiggyBank()
piggy.add_coins(100)
piggy.remove_coins(200)
print(piggy.balance)