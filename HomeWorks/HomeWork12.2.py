class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name} {self.price} {self.description} {self.dimensions}"

class User:

    def __init__(self, name, surname, numberphone, age):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}" # {self.numberphone} {self.age}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        # if item in self.products:
        #     self.products[item] += cnt
        #     if self.products[item] <= 0:
        #         del self.products[item]
        # elif cnt > 0:
        #     self.products[item] = cnt
        if cnt > 0:
            self.products[item] = cnt
        elif item in self.products and self.products[item] + cnt <= 0:
            del self.products[item]

    def get_total(self):
        total = 0
        # for item, quantity in self.products.items():
        #     total += item.price * quantity
        return sum(item.price * quantity for item, quantity in self.products.items())

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, quantity in self.products.items():
            result += f"{item.name}: {quantity} pcs.\n"
        result += f"Total: {self.get_total()} units"
        return result

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162", 34)
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40




























