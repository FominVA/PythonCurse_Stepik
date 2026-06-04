class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=None):
        self.items = []
        if items is not None:
            for item in items:
                self.add(item)

    def __str__(self):
        if not self.items:
            return ""
        return "\n".join(str(item) for item in self.items)

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.price for item in self.items)

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]


shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())